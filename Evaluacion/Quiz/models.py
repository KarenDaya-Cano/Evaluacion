from django.db import models

class Estudiante(models.Model):
    estudiante = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    edad = models.IntegerField()

    class Meta:
        verbose_name = 'estudiante'
        verbose_name_plural = 'estudiantes'

    def __str__(self):
        return self.estudiante
