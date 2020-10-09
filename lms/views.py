from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test

from datetime import datetime as dt
from .forms import RegisterForm, StudentForm, CourseCreateForm
from .models import Course, Teacher, Student, Enroll

# Create your views here.

def index(request):
    latest_course_list = Course.objects.order_by('id')
    template = loader.get_template('lms/index1.html')
    context = {
        'latest_subject_list': latest_course_list,
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


@user_passes_test(is_teacher, login_url='/lms/')
def create_course(request):
    if request.method == 'POST':
        course_form = CourseCreateForm(request.POST)
        if course_form.is_valid():
            course = course_form.save()
            return redirect('/lms/')
    else:
        course_form = CourseCreateForm()
    return render(request, 'courses/create.html', {"course_form": course_form})


def course_detail(request, course_id):
    '''subjects = Subject.objects.all()
    templates = []
    for subject in subjects:
        template = loader.get_template('lms/' + subject.id + '.html')
        templates.add(template)'''
    course = Course.objects.get(id=course_id)
    template = loader.get_template('lms/' + course.id + '.html')
    context = {
        'subject_name': course.name,
        'subject_id': course.id,
        'subject_description': 
            "Nội dung chính\n\
                \thttps://uet.vnu.edu.vn/~thanhld/lects/webappdev/\n\
            Chỉ dạy basic, không dạy frameworks\n\
                \tDẠY/Giới thiệu : HTML, CSS, JS, Bootstrap, Jquery, PHP\n\
                \tKHÔNG DẠY: React, AngularJS, NodeJS, Laravel, Express, Django, RoR\n\
            Nội dung bổ sung\n\
                \tKhuyến khích tìm hiểu frameworks (hoặc công cụ)\n\
                \tNodeJS, NPM, bower, webpack\n\
            Giới thiệu, demo, tutorial frameworks, …\n\
            How to start a project !!!"
    }
    return HttpResponse(template.render(context, request))

