from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm
from .models import Course, Teacher, Student, Enroll

# Create your views here.

def index(request):
    latest_course_list = Course.objects.order_by('id')
    template = loader.get_template('lms/index1.html')
    context = {
        'latest_subject_list': latest_course_list,
    }
    return HttpResponse(template.render(context, request))


def register(response):
    if response.method == "POST":
        form = RegisterForm()
        if form.is_valid():
            form.save()
            
        return redirect('/lms/')
    else:
        form = RegisterForm()
    return render(response, 'registration/register.html', {"form": form})

'''@receiver(post_save, sender=get_user_model())
def create_student_user(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)'''


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

