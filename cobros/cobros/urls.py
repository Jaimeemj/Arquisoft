from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas de tu aplicación
    path('cobros/', views.lista_cobros, name='lista_cobros'),
    path('suma/', views.obtener_suma_total, name='obtener_suma_total'),  # Nueva ruta
]
]
