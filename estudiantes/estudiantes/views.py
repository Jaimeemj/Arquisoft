from django.http import HttpResponse
from django.shortcuts import render
from .logic import estudiantes_logic as vl
from cobros.cobros.logic import cobros_logic as cl
from django.http import HttpResponse
from django.core import serializers
import requests

def estudiantes(request):
    if request.method == 'GET':
        estudiantes = vl.get_estudiantes()
        estudiantes.dto = serializers.serialize('json', estudiantes)
        return HttpResponse(estudiantes.dto, 'application/json')
        

def estudiantes_list(request):
    estudiantes = vl.get_estudiantes()
    context = {
        'estudiantes_list': estudiantes
    }
    return render(request, 'estudiantes.html', context)

def cobros_estudiante(request, estudiante_id):
    estudiante = vl.get_estudiante(estudiante_id)
    cobros = cl.get_cobros(estudiante)
    return render(request, 'cobros.html', {'estudiante': estudiante, 'cobros': cobros})
# Create your views here.


