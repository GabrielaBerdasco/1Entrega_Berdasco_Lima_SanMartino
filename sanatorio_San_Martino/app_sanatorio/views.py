from django.shortcuts import render
from app_sanatorio.models import Medico, Paciente, ObrasSociales
from app_sanatorio.forms import MedicoFormulario, CrearPaciente, ObrasFormulario


def inicio(request) :
    return render(request, "app_sanatorio/inicio.html")

def crear_paciente(request) :

    if request.method == 'POST':
            formulario = CrearPaciente(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  paciente = Paciente(nombre=data['nombre'], apellido=data['apellido'], fecha_nacimiento=data['fecha_nacimiento'], ciudad=data['ciudad'], telefono=data['telefono'], email=data['email'])
                  paciente.save()

                  return render(request, "App_sanatorio/inicio.html", {"exitoso": True})
    else:  
            formulario= CrearPaciente()  
            
    return render(request, "App_sanatorio/cargar_medico.html", {"formulario": formulario})


def obras_sociales(request) :
    return render(request, "app_sanatorio/obras-sociales.html")

def obras_formulario(request) :
    if request.method == 'POST':
            formulario = ObrasFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  obra = ObrasSociales(nombre=data['nombre'], telefono=data['telefono'], email=data['email'])
                  return render(request, "App_sanatorio/inicio.html", {"exitoso": True})
    else:  
            formulario= ObrasFormulario()  
    return render(request, "App_sanatorio/obras_sociales.html", {"formulario": formulario})


def busquedaEspecialidad(request) :
    return render(request, "app_sanatorio/consulta.html")


def buscar(request) :

    if request.GET["especialidad"] :

        especialidad = request.GET["especialidad"]
        medico = Medico.objects.filter(especialidad__icontains = especialidad)
        return render(request, "App_sanatorio/resultado.html", {"medico": medico})

    else:

        return render(request, "App_sanatorio/consulta.html", {"medico": []})


def medicos(request) :
    return render(request, "app_sanatorio/medicos.html")


def medicos_formulario(request):
    if request.method == 'POST':
            formulario = MedicoFormulario(request.POST)

            if formulario.is_valid():
                  data = formulario.cleaned_data
                  medico = Medico(nombre=data['nombre'], apellido=data['apellido'], especialidad=data['especialidad'], email=data['email'])
                  medico.save()
                  return render(request, "App_sanatorio/inicio.html", {"exitoso": True})
    else:  
            formulario= MedicoFormulario()  
    return render(request, "App_sanatorio/cargar_medico.html", {"formulario": formulario})