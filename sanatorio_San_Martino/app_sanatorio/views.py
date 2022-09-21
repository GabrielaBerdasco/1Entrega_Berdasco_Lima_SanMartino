from django.shortcuts import render
from app_sanatorio.models import Medico
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app_sanatorio.models import Blog
from django.urls import reverse, reverse_lazy




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


class BlogCreateView(CreateView):
    model = Blog
    fields = ["titulo", "subtitulo", "autor", "cuerpo", "fecha", "imagen"]
    success_url = reverse_lazy('inicio')


class BlogListView(ListView) :
    model = Blog
    template_name = "app_sanatorio/blog_list.html"