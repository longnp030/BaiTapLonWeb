from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('courses/<int:course_id>', views.course_detail, name='course_detail'),
] + static('lms/images/student_images', document_root=settings.STUDENT_IMAGE_DIR)