from django.shortcuts import render

from app_sanatorio.models import Medico
from app_sanatorio.forms import MedicoFormulario


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


def medicos_formulario(request):

    if request.method == 'POST':
            formulario = MedicoFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  medico = Medico(nombre=data['nombre'], apellido=data['apellido'], especialidad=data['especialidad'], email=data['email'])
                  medico.save()

                  return render(request, "app_sanatorio/inicio.html", {"exitoso": True})
    else:  
            formulario= MedicoFormulario()  
            
    return render(request, "app_sanatorio/cargar_datos.html", {"formulario": formulario})