from .models import Cobro
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
import json

def check_estudiante(data):
    r = requests.get(settings.PATH_EST, headers={"Accept":"application/json"})
    estudiantes = r.json()
    for estudiante in estudiantes:
        if data["estudiante"] == estudiante["id"]:
            return True
    return False


def CobrosList(request):
    queryset = Cobro.objects.all()
    context = list(queryset.values('id', 'estudiante', 'monto', 'pagado'))
    return JsonResponse(context, safe=False)

def CobrosPage(request):
    return render(request, 'cobros.html')
