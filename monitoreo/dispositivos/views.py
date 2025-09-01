from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Dispositivo
from .forms import DispositivoForm


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

def crear_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm()

    return render(request, 'dispositivos/crear.html', {'form': form})

def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('listar_dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, 'dispositivos/editar.html', {'form': form})
    
def eliminar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('listar_dispositivos')
    return render(request, 'dispositivos/eliminar.html', {'dispositivo': dispositivo})
