from django.shortcuts import render
from django.http import HttpResponse


def inicio(request):
    contexto = {"nombre" : "developer Felipe "}
    productos = [
        {"nombre": "Sensor 1", "valor": 100},
        {"nombre": "Sensor 2", "valor": 200},
        {"nombre": "Sensor 3", "valor": 300}
    ]
    return render(request,"dispositivos/inicio.html", {"contexto": contexto, "productos": productos})

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
