from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre, self.comision
    

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre, self.apellido
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    profesion = models.CharField(max_length=140)

    def __str__(self):
        return self.nombre, self.apellido
    

class Entregable(models.Model):
    nombre = models.CharField(max_length=200)
    esta_aprobado = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre