import django
from lms.views import change_password
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/change_password/', views.change_password, name='change_password'),
    path('accounts/change_password_done/', views.change_password_done, name='change_password_done'),
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/register-as-teacher/', views.teacher_register, name='teacher_register'),
    path('accounts/register_done', views.register_done, name='register_done'),
    path('courses/add/', views.create_course, name='create_course'),
    path('courses/<int:course_id>/enroll/', views.course_enroll, name='enroll'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/<int:course_id>/', views.course_overview, name='course_overview'),
    path('search/', views.search_result, name='search'),
    path('files/<str:file_path>', views.view_file, name='view_file'),
    path('<obj_id>/delete/', views.delete_obj, name='delete_obj'),
    path('<obj_id>/modify/', views.modify_obj, name='modify_obj'),
    path('courses/<int:course_id>/add_lecture/', views.add_lecture, name='add_lecture'),
    # path('courses/<int:course_id>/lecture/<int:lecture_id>/add_unit/', views.add_unit, name='add_unit'),  # 17/12
    path('users/<int:user_id>', views.user_profile, name='user_profile'),
    path('db/', views.db_import, name='db_import'),
] + static('images', document_root=settings.IMAGE_DIR)