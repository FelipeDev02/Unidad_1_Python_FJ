from django.db import models #los imports

# Create your models here.

class BaseModel(models.Model):
    ESTADOS = [
        ("ACTIVO", "Activo"),
        ("INACTIVO", "Inactivo"),
    ]

    estado = models.CharField(max_length=10, choices=ESTADOS, default="ACTIVO")
    created_at = models.DateTimeField(auto_now_add=True)  # se asigna al crear
    updated_at = models.DateTimeField(auto_now=True)  # se actualiza cada vez que se guarda
    deleted_at = models.DateTimeField(null=True, blank=True)  # opcional para borrado lógico

    class Meta:
        abstract = True  # no crea tabla, solo se hereda

class Categoria(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class Zona(BaseModel):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Dispositivo(BaseModel):
    nombre = models.CharField(max_length=100)
    consumo = models.FloatField()
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class Medicion(BaseModel):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, related_name="mediciones")
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo = models.FloatField(help_text="Consumo registrado")

    def __str__(self):
        return f"{self.dispositivo} - {self.fecha_hora} - Consumo:{self.consumo} "
    
class Alerta(BaseModel):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_hora = models.DateTimeField(auto_now_add=True)
    consumo_detectado = models.FloatField(help_text="Consumo detectado")


#modelos listos

