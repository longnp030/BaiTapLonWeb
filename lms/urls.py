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
    path('accounts/register-as-teacher/', views.teacher_register, name='teacher_register'),
    path('courses/add/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/enroll/', views.course_enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/<int:course_id>/', views.course_overview, name='course_overview'),
    path('files/<str:file_path>', views.view_file, name='view_file'),
    path('<obj_id>/delete/', views.delete_obj, name='delete_obj'),
    path('<obj_id>/modify/', views.modify_obj, name='modify_obj'),
    path('users/<int:user_id>', views.user_profile, name='user_profile')
] + static('images/users', document_root=settings.USERS_IMAGE_DIR) \
  + static('images/courses', document_root=settings.COURSES_IMAGE_DIR)