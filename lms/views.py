from django.contrib.auth.forms import PasswordChangeForm
from django.core.checks import messages
from django.core.mail import send_mail
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.dispatch import receiver
from django.apps import AppConfig as conf
from django.urls import reverse
from django.db.models.signals import post_save
from django.contrib.auth import authenticate, get_user_model, update_session_auth_hash, login
from django.contrib.auth.decorators import login_required, user_passes_test

import datetime as dt

from .forms import *
from .models import *

from eLearning.settings import ENROLLED_REDIRECT_URL, EMAIL_HOST_USER

import random

# Create your views here.

def get_student(request):
    if request.user.is_authenticated and not request.user.is_staff and not request.user.is_admin:
        this_student = Student.objects.get(email=request.user.email)
        return this_student
    return None

def get_teacher(request):
    if request.user.is_authenticated and (request.user.is_staff or request.user.is_admin):
        this_teacher = Teacher.objects.get(email=request.user.email)
        return this_teacher
    return None


def index(request):
    template = loader.get_template('lms/index1.html')

    latest_course_list = Course.objects.order_by('id')
    context = {}
    this_student = get_student(request)
    this_teacher = get_teacher(request)
    this_user = None
    if this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher
    context = {
        'latest_course_list': latest_course_list,
    }
    if this_user is not None:
        context['this_user'] = this_user
    return HttpResponse(template.render(context, request))


def register(request):
    if request.user.is_authenticated:
        return redirect('/lms/')

    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        student_form = StudentForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.id = user.id
            student.name = student.name
            student.email = user.email
            student.joindate = dt.datetime.now()
            student.useremail = user
            student.save()

            send_mail(
                subject="Learning Management System Account Register",
                message="Hi,\n"
                        "Your account has been created.\n" +
                        "Please read our policies and rules to participate joyfully in our learning community!\n\n" +
                        "Sincerely,\n" +
                        "Learning Management System",
                from_email=EMAIL_HOST_USER,
                recipient_list=[student.email, ],
                fail_silently=False,
            )

            return redirect('register_done')
    else:
        user_form = RegisterForm()
        student_form = StudentForm()
    
    return render(request, 'registration/register.html', {"user_form": user_form, "student_form": student_form})


def teacher_register(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('/lms/')
    if request.method == 'POST':
        user_form = TeacherRegisterForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()

            teacher = teacher_form.save(commit=False)
            teacher.id = user.id
            teacher.name = teacher.name
            teacher.email = user.email
            teacher.joindate = dt.now()
            teacher.useremail = user
            teacher.save()

            return redirect('register_done')
    else:
        user_form = TeacherRegisterForm()
        teacher_form = TeacherForm()
    return render(request, 'registration/teacher_register.html', {"user_form": user_form, "teacher_form": teacher_form})    


def register_done(request):
    return render(request, 'registration/register_done.html', {})


def is_teacher(user):
    return user.is_authenticated and (user.is_staff or user.is_admin)

@user_passes_test(is_teacher, login_url='/lms/accounts/login/')
def create_course(request):
    this_user = get_teacher(request)
    if request.method == 'POST':
        course_form = CourseCreateForm(request.POST)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.publishDate = dt.datetime.now()
            course.save()

            teach = Teach(teacher=this_user, course=course)
            teach.save()

            return redirect('/lms/')
    else:
        course_form = CourseCreateForm()
    return render(request, 'courses/create.html', {"course_form": course_form, "this_user": this_user})


@login_required(login_url='/lms/accounts/login/')
def course_enroll(request, course_id):
    current_course = Course.objects.get(id=course_id)
    current_user = request.user
    current_student = Student.objects.get(email=current_user.email)

    course_isEnrolled_count = Enroll.objects.filter(course=current_course.id)
    student_isEnrolled_count = course_isEnrolled_count.filter(student=current_student.id)
    if len(course_isEnrolled_count) > 0 and len(student_isEnrolled_count) > 0:
        return render(request, 'courses/enroll.html', {"already_enrolled": True, "course_id": current_course.id})

    if request.method == 'POST':
        enrollment_form = EnrollmentForm(request.POST)
        if enrollment_form.is_valid():
            enrollment = enrollment_form.save(commit=False)
            enrollment.student = current_student
            enrollment.course = current_course
            enrollment.save()

            return redirect(ENROLLED_REDIRECT_URL)
    else:
        enrollment_form = EnrollmentForm(initial={'student': current_student, 'course': current_course})
    return render(request, 'courses/enroll.html', {"enrollment_form": enrollment_form, "course_id": current_course.id, "this_user": current_user})


@login_required(login_url='/lms/accounts/login/')
def dashboard(request):
    this_student = get_student(request)
    this_teacher = get_teacher(request)
    this_user = None
    if this_teacher is None and this_student is None:
        return redirect('/lms/')
    elif this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher
    
    course_list = []
    if isinstance(this_user, Student):
        this_student_enrollments = Enroll.objects.filter(student=this_user.id)
        for enrollment in this_student_enrollments:
            course_list.append(Course.objects.get(id=enrollment.course.id))
    elif isinstance(this_user, Teacher):
        # course_list = Course.objects.filter(teacher=this_user.id)
        course_list = [ti.course for ti in Teach.objects.filter(teacher=this_teacher)] # changed 12/11 bcof adding new table
    context = {
        "my_courses": course_list,
        "this_user": this_user,
    }
    return render(request, 'courses/dashboard.html', context=context)


def course_overview(request, course_id):
    course = Course.objects.get(id=course_id)
    this_student = get_student(request)
    this_teacher = get_teacher(request)

    can_modify_obj = False
    this_user = None
    context = {}
    enrolled = False
    if this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher
    if isinstance(this_user, Student):
        this_course_enrollments = Enroll.objects.filter(course=course.id)
        enrolled = len(this_course_enrollments.filter(student=this_user.id)) > 0
    elif isinstance(this_user, Teacher):
        teach = Teach.objects.filter(course=course_id)
        if len(teach) == 0:
            enrolled = False
        else:
            enrolled = teach[0].teacher.id == this_user.id
    
    unit_form = None
    lecture_form = None
    lecture_form_initial = {'course': course,}
    unit_form_initial = {'lecture': Lecture.objects.filter(course=course)[0] if len(Lecture.objects.filter(course=course)) > 0 else None,}
    
    if this_teacher:
        if request.method == 'POST':
            if 'add_unit' in request.POST:
                unit_form = UnitCreateForm(request.POST)
                unit_form.fields['lecture'].queryset = Lecture.objects.filter(course=course)
                if unit_form.is_valid():
                    unit_form.save()
                    unit_form = UnitCreateForm(initial=unit_form_initial)
            
            if 'add_lect' in request.POST:
                lecture_form = LectureCreateForm(request.POST)
                lecture_form.fields['course'].queryset = Course.objects.filter(id=course.id)
                if lecture_form.is_valid():
                    lecture_form.save()
                    lecture_form = LectureCreateForm(initial=lecture_form_initial)
        else:
            unit_form = UnitCreateForm(initial=unit_form_initial, )
            unit_form.fields['lecture'].queryset = Lecture.objects.filter(course=course)
            lecture_form = LectureCreateForm(initial=lecture_form_initial)
            lecture_form.fields['course'].queryset = Course.objects.filter(id=course.id)
        
        can_modify_obj = True

    context = {
        "course": course,
        "enrolled": enrolled,
        "this_user": this_user,
        "detail": course_detail(course_id) if enrolled else None,
        "lecture_form": lecture_form,
        "unit_form": unit_form,
        "can_modify_obj": can_modify_obj,
        "teach": Teach.objects.filter(course=course.id)[0] if len(Teach.objects.filter(course=course.id)) > 0 else None,
    }
    return render(request, 'courses/course_overview.html', context=context)


'''def add_lect(request):
    if request.method == 'POST':
        lecture_form = LectureCreateForm(request.POST)
        if lecture_form.is_valid():
            lecture_form.save()
            return redirect('/lms/')
    else:
        lecture_form = LectureCreateForm()
    return render(request, 'courses/create_lect.html', context=lecture_form)
def add_unit(request):
    if request.method == 'POST':
        unit_form = UnitCreateForm(request.POST)
        if unit_form.is_valid():
            unit_form.save()
            return redirect('/lms/')
    else:
        unit_form = UnitCreateForm()
    return render(request, 'courses/create_unit.html', context=unit_form)'''


def course_detail(course_id):
    this_course = Course.objects.get(id=course_id)
    this_course_lectures = Lecture.objects.filter(course=this_course.id)
    lectures = []
    for lecture in this_course_lectures:
        lectures.append({
            "lecture": lecture,
            "units": Unit.objects.filter(lecture=lecture.id),
        })
    teach = Teach.objects.filter(course=this_course.id)
    teacher = None
    if len(teach) <= 0 :
        teach = None
    else:
        teach = teach[0]
        teacher = teach.teacher
    this_course_enrollments = Enroll.objects.filter(course=this_course.id)
    classmates = [this_course_enrollment.student for this_course_enrollment in this_course_enrollments]
    detail = {"lectures": lectures, "teacher": teacher, "classmates": classmates, }
    return detail

def modify_obj(request, obj_id):
    obj = Unit.objects.get(id=obj_id)
    if obj is None:
        obj = Lecture.objects.get(id=obj_id)
        if obj is None:
            obj = Assignment.objects.get(id=obj_id)
    obj_change_form = None
    if request.method == 'POST':
        if isinstance(obj, Unit):
            obj_change_form = UnitCreateForm(request.POST, instance=obj)
        elif isinstance(obj, Lecture):
            obj_change_form = LectureCreateForm(request.POST, instance=obj)
        elif isinstance(obj, Assignment):
            obj_change_form = AssignmentCreateForm(request.POST, instance=obj)
        if obj_change_form.is_valid():
            obj_change_form.save()
            return redirect('/lms/')
    else:
        if isinstance(obj, Unit):
            obj_change_form = UnitCreateForm(instance=obj)
        elif isinstance(obj, Lecture):
            obj_change_form = LectureCreateForm(instance=obj)
        elif isinstance(obj, Assignment):
            obj_change_form = AssignmentCreateForm(instance=obj)
    return render(request, 'courses/modify_comps.html', context={"obj_change_form": obj_change_form, })

def delete_obj(request, obj_id):
    obj = Unit.objects.get(id=obj_id)
    if obj is None:
        obj = Lecture.objects.get(id=obj_id)
        if obj is None:
            obj = Assignment.objects.get(id=obj_id)
    obj.delete()
    return HttpResponseRedirect('')


'''@login_required
def course_detail(request, course_id):
    this_course = Course.objects.get(id=course_id)
    this_student = get_student(request)
    this_teacher = get_teacher(request)
    this_user = None
    if this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher

    context = {}
    this_course_lectures = Lecture.objects.filter(course=this_course.id)
    lectures = []
    for lecture in this_course_lectures:
        lectures.append({
            "lecture": lecture,
            "units": Unit.objects.filter(lecture=lecture.id),
        })
    context = {
        "lectures": lectures,
        "this_user": this_user,
    }
    return render(request, 'courses/course_detail.html', context=context)'''


def view_file(request, file_path):
    return FileResponse(open(file_path, 'rb'), content_type='application/pdf')


#@login_required(login_url='/lms/accounts/login/')
def user_profile(request, user_id):
    this_user = Student.objects.get(email=request.user.email) if len(Student.objects.filter(email=request.user.email)) > 0 else Teacher.objects.get(email=request.user.email)
    this_student = Student.objects.filter(id=user_id)
    this_teacher = Teacher.objects.filter(id=user_id)
    context = {
        "this_user": this_user,
    }
    form = None
    if len(this_student) > 0 and len(this_teacher) == 0:
        this_student = this_student[0]
        this_teacher = None
        context["this_student"] = this_student
    elif len(this_student) == 0 and len(this_teacher) > 0:
        this_student = None
        this_teacher = this_teacher[0]
        context["this_teacher"] = this_teacher
    else:
        this_student = None
        this_teacher = None

    if request.method == 'POST':
        if this_student is not None:
            form = StudentInfoForm(request.POST, request.FILES)
            if form.is_valid():
                this_student.image = request.FILES.get('image') if request.FILES.get('image') is not None else this_student.image
                this_student.facebook = form.cleaned_data['facebook'] if len(form.cleaned_data['facebook']) > 0 else this_student.facebook
                this_student.twitter = form.cleaned_data['twitter'] if len(form.cleaned_data['twitter']) > 0 else this_student.twitter
                this_student.website = form.cleaned_data['website'] if len(form.cleaned_data['website']) > 0 else this_student.website
                this_student.save()
                return redirect(reverse('user_profile', kwargs={'user_id': this_student.id}))
        elif this_teacher is not None:
            form = TeacherInfoForm(request.POST, request.FILES)
            if form.is_valid():
                this_teacher.image = request.FILES.get('image') if request.FILES.get('image') is not None else this_teacher.image
                this_teacher.facebook = form.cleaned_data['facebook'] if len(form.cleaned_data['facebook']) > 0 else this_teacher.facebook
                this_teacher.twitter = form.cleaned_data['twitter'] if len(form.cleaned_data['twitter']) > 0 else this_teacher.twitter
                this_teacher.website = form.cleaned_data['website'] if len(form.cleaned_data['website']) > 0 else this_teacher.website
                this_teacher.save()
                return redirect(reverse('user_profile', kwargs={'user_id': this_teacher.id}))
    else:
        if this_student is not None:
            form = StudentInfoForm()
        elif this_teacher is not None:
            form = TeacherInfoForm()
    context['form'] = form
    return render(request, "lms/user_profile.html", context=context)


@login_required(login_url='/lms/accounts/login/')
def change_password(request):
    this_student = get_student(request)
    this_teacher = get_teacher(request)
    this_user = None
    if this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request=request, user=user)
            messages.Info(request, 'Your password was successfully updated!')
            return redirect('change_password_done')
        else:
            messages.Error(request, 'Please correct the error below!')
    else:
        form = PasswordChangeForm(request.user)

    context = {"form": form, "this_user": this_user, }
    return render(request, 'registration/change_password.html', context)


def change_password_done(request):
    this_student = get_student(request)
    this_teacher = get_teacher(request)
    this_user = None
    if this_student is not None and this_teacher is None:
        this_user = this_student
    elif this_student is None and this_teacher is not None:
        this_user = this_teacher
    context = {'this_user': this_user, }
    return render(request, 'registration/change_password_done.html', context)


def forgot_password(request):
    pass


def db_import(request):
    with open('lms/data/courses.txt', 'r') as f:
        courses = [course_txt[1:] for course_txt in f.read().split('}\n')]

        for course in courses:
            try:
                description = course.split(",\n ")[0].split("': '")[1][:-1].replace("'", '').replace('\n', ' ').strip()
                while '  ' in description:
                    description = description.replace('  ', ' ')
                name = course.split(",\n ")[1].split("': '")[1][:-1].replace("'", '').replace('\n', ' ').strip()
                while '  ' in name:
                    name = name.replace('  ', ' ')
                publishdate = course.split(",\n ")[3].split("': '")[1][:-1].replace("'", '').replace('\n', ' ').strip().split()
                # 16th Nov, 2020
                publishdate_day = publishdate[0][:-2]
                publishdate_month = publishdate[1][:-1]
                if publishdate_month == 'Jan':
                    publishdate_month = 1
                elif publishdate_month == 'Feb':
                    publishdate_month = 2
                elif publishdate_month == 'Mar':
                    publishdate_month = 3
                elif publishdate_month == 'Apr':
                    publishdate_month = 4
                elif publishdate_month == 'May':
                    publishdate_month = 5
                elif publishdate_month == 'Jun':
                    publishdate_month = 6
                elif publishdate_month == 'Jul':
                    publishdate_month = 7
                elif publishdate_month == 'Aug':
                    publishdate_month = 8
                elif publishdate_month == 'Sep':
                    publishdate_month = 9
                elif publishdate_month == 'Oct':
                    publishdate_month = 10
                elif publishdate_month == 'Nov':
                    publishdate_month = 11
                elif publishdate_month == 'Dec':
                    publishdate_month = 12
                publishdate_year = publishdate[2]
                publishdate = publishdate_year + '-' + str(publishdate_month) + '-' + publishdate_day
                c = Course()
                c.id = random.randint(5, 100000)
                while len(Course.objects.filter(id=c.id)) > 0:
                    c.id = random.randint(5, 100000)
                c.name = name
                c.description = description
                c.publishdate = publishdate
                c.price = 0
                try:
                    c.save()
                    print('Saved')
                except Exception as e:
                    print(e)
                    print('Save failed')
            except Exception as e:
                print(e)
    return HttpResponse(request)