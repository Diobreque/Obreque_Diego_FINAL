from django.db import models

# Create your models here.

from django.db import models

class Institucion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_institucion = models.CharField(max_length=100)


class Inscrito(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    fecha_inscripcion = models.DateField()
    institucion = models.ForeignKey('Institucion', on_delete=models.CASCADE)
    hora_inscripcion = models.TimeField()
    estado = models.CharField(max_length=10, choices=ESTADOS)
    observacion = models.TextField()

