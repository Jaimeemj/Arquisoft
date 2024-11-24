from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('estudiantes/', views.estudiantes_list, name='estudiantes_list'),
    path('estudiante/<int:estudiante_id>/cobros/', views.cobros_estudiante, name='cobros_estudiante'),
]
