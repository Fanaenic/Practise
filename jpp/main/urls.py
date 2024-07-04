from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('resumes/', views.resumes, name='resumes'),
]
