from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime as dt

from .forms import RegisterForm, StudentForm, CourseCreateForm, EnrollmentForm
from .models import Course, Teacher, Student, Enroll

from eLearning.settings import ENROLLED_REDIRECT_URL, ENROLLED_INDEXES

import random

# Create your views here.

def index(request):
    latest_course_list = Course.objects.order_by('id')
    template = loader.get_template('lms/index1.html')
    context = {
        'latest_course_list': latest_course_list,
    }
    return HttpResponse(template.render(context, request))


'''def register(response):
    if response.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
            
        return redirect('/lms/')
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form": form})'''


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


'''@receiver(post_save, sender=get_user_model())
def create_student_user(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)'''


def is_teacher(user):
    return user.is_authenticated and user.admin == True


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


def course_enroll(request, course_id):
    current_course = Course.objects.get(id=course_id)
    current_user = request.user
    current_student = Student.objects.get(email=current_user.email)

    course_isEnrolled_count = Enroll.objects.filter(courseid=current_course.id)
    student_isEnrolled_count = course_isEnrolled_count.filter(studentid=current_student.id)
    if len(course_isEnrolled_count) > 0 and len(student_isEnrolled_count) > 0:
        return render(request, 'courses/enroll.html', {"already_enrolled": True, "course_id": current_course.id})

    if request.method == 'POST':
        enrollment_form = EnrollmentForm(request.POST)
        if enrollment_form.is_valid():
            enrollment = enrollment_form.save(commit=False)
            enrollment.studentid = current_student
            enrollment.courseid = current_course
            enrollment.save()

            return redirect(ENROLLED_REDIRECT_URL)
    else:
        new_id = random.randint(1, 1000)
        while new_id in ENROLLED_INDEXES:
            new_id = random.randint(1, 1000)
        ENROLLED_INDEXES.append(new_id)
        enrollment_form = EnrollmentForm(initial={'id': new_id, 'studentid': current_student, 'courseid': current_course})
    return render(request, 'courses/enroll.html', {"enrollment_form": enrollment_form, "course_id": current_course.id})


@login_required(login_url='/lms/accounts/login/')
def my_courses(request):
    this_student_qs = Student.objects.filter(email=request.user.email)
    if len(this_student_qs) == 0:
        return redirect('/lms/')
    this_student = this_student_qs[0]
    this_student_enrollments = Enroll.objects.filter(studentid=this_student.id)
    this_student_courses = []
    for enrollment in this_student_enrollments:
        this_student_courses.append(Course.objects.get(id=enrollment.courseid.id))
    return render(request, 'courses/my_courses.html', {"my_courses": this_student_courses})


def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    course_info = {
        'course_id': course.id,
        'course_name': course.name,
        'course_teacher': course.teacherid.name,
        'course_description': course.description,
        'course_price': course.price,
    }

    this_course_enrollments = Enroll.objects.filter(courseid=course.id)
    this_student_qs = Student.objects.filter(email=request.user.email)
    this_student_enrolled = 0
    if len(this_student_qs) == 0:
        return redirect('/lms/')
        #pass
    else:
        this_student = this_student_qs[0]
        this_student_enrolled = len(this_course_enrollments.filter(studentid=this_student.id))

    enrolled = False
    if this_student_enrolled > 0:
        enrolled = True
    return render(request, 'courses/course_detail.html', {"course_info": course_info, "enrolled": enrolled})