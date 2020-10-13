from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime as dt

from .forms import *
from .models import *

from eLearning.settings import ENROLLED_REDIRECT_URL, ENROLLED_INDEXES

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
            student.joindate = dt.now()
            student.useremail = user
            student.save()

            return redirect('/lms/')
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

            return redirect('/lms/')
    else:
        user_form = TeacherRegisterForm()
        teacher_form = TeacherForm()
    return render(request, 'registration/teacher_register.html', {"user_form": user_form, "teacher_form": teacher_form})    


def is_teacher(user):
    return user.is_authenticated and (user.is_staff or user.is_admin)

@user_passes_test(is_teacher, login_url='/lms/accounts/login/')
def create_course(request):
    if request.method == 'POST':
        course_form = CourseCreateForm(request.POST)
        if course_form.is_valid():
            course = course_form.save(commit=False)
            course.publishDate = dt.now()
            course.save()
            return redirect('/lms/')
    else:
        course_form = CourseCreateForm()
    return render(request, 'courses/create.html', {"course_form": course_form})


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
        new_id = random.randint(1, 1000)
        while new_id in ENROLLED_INDEXES:
            new_id = random.randint(1, 100000)
        ENROLLED_INDEXES.append(new_id)
        enrollment_form = EnrollmentForm(initial={'id': new_id, 'student': current_student, 'course': current_course})
    return render(request, 'courses/enroll.html', {"enrollment_form": enrollment_form, "course_id": current_course.id})


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
        course_list = Course.objects.filter(teacherid=this_user.id)
    context = {
        "my_courses": course_list,
        "this_user": this_user,
    }
    return render(request, 'courses/dashboard.html', context=context)


def course_overview(request, course_id):
    course = Course.objects.get(id=course_id)
    this_student = get_student(request)
    this_teacher = get_teacher(request)

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
        enrolled = len(Course.objects.filter(teacherid=this_user.id).filter(teacherid=this_user.id)) > 0
    context = {
        "course": course,
        "enrolled": enrolled,
        "this_user": this_user,
        "lectures": course_detail(course_id) if enrolled else None,
    }
    return render(request, 'courses/course_overview.html', context=context)


def course_detail(course_id):
    this_course = Course.objects.get(id=course_id)
    this_course_lectures = Lecture.objects.filter(course=this_course.id)
    lectures = []
    for lecture in this_course_lectures:
        lectures.append({
            "lecture": lecture,
            "units": Unit.objects.filter(lecture=lecture.id),
        })
    return lectures

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
    #this_course_lectures_units = []
    lectures = []
    for lecture in this_course_lectures:
        #this_course_lectures_units.append(Unit.objects.filter(lecture=lecture.id))
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
    return render(request, "lms/user_profile.html", context=context)