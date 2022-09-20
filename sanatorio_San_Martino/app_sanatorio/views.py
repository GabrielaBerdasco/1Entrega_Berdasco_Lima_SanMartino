from django.shortcuts import render
from app_sanatorio.models import Medico



def inicio(request) :
    return render(request, "app_sanatorio/inicio.html")

def nosotros(request) :
    return render(request, "app_sanatorio/nosotros.html")

def busquedaEspecialidad(request) :
    return render(request, "app_sanatorio/consulta.html")


def buscar(request) :

    if request.GET["especialidad"] :

        especialidad = request.GET["especialidad"]
        medico = Medico.objects.filter(especialidad__icontains = especialidad)
        return render(request, "app_sanatorio/resultado.html", {"medico": medico})

    else:

        return render(request, "app_sanatorio/consulta.html", {"medico": []})
