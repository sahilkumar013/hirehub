from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('create/', views.create_job, name='create_job'),
    path('register/', views.register, name='register'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('logout/', views.logout_view, name='logout'),
]