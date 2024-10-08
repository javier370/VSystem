from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Persona

def get_estudiantes(request):

    estudiantes = Persona.objects.filter(rol='Estudiante');
    # select * from persona where rol = 'Estudiante';

    return render(request, 'lista-estudiantes.html', {
            'tittle': 'Lista de Estudiantes',
            'estudiantes': estudiantes
        })
