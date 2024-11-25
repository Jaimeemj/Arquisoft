from .models import Estudiante
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def EstudiantesList(request):
    queryset = Estudiante.objects.all()
    context = list(queryset.values('id', 'nombre', 'apellido', 'edad', 'correo', 'estado'))
    return JsonResponse(context, safe=False)


def EstudiantesPage(request):
    return render(request, 'estudiantes.html')
