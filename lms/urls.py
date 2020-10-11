from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/teach-as-teacher/', views.teacher_register, name='teacher_register'),
    path('courses/add/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/enroll/', views.course_enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('users/<int:student_id>', views.student_profile, name='student_profile')
] + static('images/student_images', document_root=settings.STUDENT_IMAGE_DIR)