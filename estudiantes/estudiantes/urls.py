from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes_api/', views.EstudiantesList, name='estudiantes_list'),
    path('estudiantes/', views.EstudiantesPage, name='estudiantes_page'),
]
