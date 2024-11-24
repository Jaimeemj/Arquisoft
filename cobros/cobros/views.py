from django.shortcuts import render
from django.http import HttpResponse
from .logic import cobros_logic as cl
from estudiantes.estudiantes.logic import estudiantes_logic as el
import requests
from django.http import JsonResponse

CALCULOS_URL = "http://10.128.0.84:8080/sum"  # Cambia la IP y puerto según sea necesario


def lista_cobros(request):
    estudiantes = el.get_estudiantes()
    estudiantes_con_cobros = []

    for estudiante in estudiantes:
        cobros = cl.get_cobros(estudiante)  
        estudiantes_con_cobros.append({
            'estudiante': estudiante,
            'cobros': cobros,
        })

    # Pasar los estudiantes y sus cobros al template
    return render(request, 'cobros2.html', {'estudiantes_con_cobros': estudiantes_con_cobros})
# Create your views here.

def obtener_suma_total(request):
    try:
        # Realizar una solicitud GET al microservicio de Cálculos
        response = requests.get(CALCULOS_URL)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            suma_total = response.json().get("suma_total", 0)  # Obtener la suma del JSON
            return JsonResponse({"suma_total": suma_total}, status=200)
        else:
            return JsonResponse({"error": "No se pudo obtener la suma total"}, status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)
