from django.shortcuts import render
from app_sanatorio.models import Medico



def inicio(request) :
    return render(request, "app_sanatorio/inicio.html")


def busquedaEspecialidad(request) :
    return render(request, "app_sanatorio/consulta.html")


def buscar(request) :

    if request.GET["especialidad"] :

        especialidad = request.GET["especialidad"]
        medico = Medico.objects.filter(especialidad__icontains = especialidad)
        return render(request, "app_sanatorio/resultado.html", {"medico": medico})

    else:

        return render(request, "app_sanatorio/consulta.html", {"medico": []})

""" def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_sanatorio/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()  # Formulario vacio para construir el html
    context = {
        'form': formulario,
        'mensaje': mensaje
    }

    return render(request, "app_sanatorio/registro.html", context=context) """