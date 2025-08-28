from django.contrib import admin

# Register your models here.
from .models import Categoria, Zona, Dispositivo, Medicion, Alerta

admin.site.register([Categoria, Zona, Medicion, Alerta])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'consumo', 'estado', 'categoria', 'zona')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre', 'consumo')