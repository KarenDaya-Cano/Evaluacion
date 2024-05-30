from django.shortcuts import render
from Quiz.models import Estudiante

def Tabla (request):
    lista = Estudiante.objects.all()
    return render(request, 'tabla.html',{'estudiante':lista})