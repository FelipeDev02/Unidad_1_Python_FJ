from django.shortcuts import render
from django.http import HttpResponse
from .models import Dispositivo


def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria") #join
    
    return render(request, "dispositivos/inicio.html", {"dispositivos": dispositivos})

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    return render(request, "dispositivos/dispositivo.html", {"d": dispositivo})

def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "Sensor Temperatura", "consumo": 120},
        {"nombre": "Medidor Solar", "consumo": 200},
        {"nombre": "Sensor Movimiento", "consumo": 50},
        {"nombre": "Calefactor", "consumo": 350}
    ]

    consumo_maximo = 200

    return render(request, "dispositivos/panel.html", {"dispositivos": dispositivos, "consumo_maximo": consumo_maximo})
# Create your views here.
