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
    path('courses/add/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/enroll/', views.course_enroll, name='enroll'),
    path('courses/my/', views.my_courses, name='my_courses'),
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
] + static('images/student_images', document_root=settings.STUDENT_IMAGE_DIR)