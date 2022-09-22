from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from app_blog.models import Blog, Comentario
from app_blog.forms import ComentarioFormulario



class BlogCreateView(CreateView):
    model = Blog
    fields = ["titulo", "subtitulo", "cuerpo", "imagen"]
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class BlogListView(ListView) :
    model = Blog
    template_name = "app_blog/blog_list.html"


def ver_articulo(request, id):
    
    articulo = Blog.objects.get(id=id)
    comentarios = Comentario.objects.filter(articulo = articulo.id)
    contexto = {
        'articulo': articulo,
        'comentarios': comentarios
    }

    return render(request, "app_blog/articulo.html", contexto)


#editar articulo, eliminar articulo
    
def comentario_form(request, id) :
    
    articulo = Blog.objects.get(id=id)

    if request.method == 'POST':
        formulario = ComentarioFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comentario = Comentario(cuerpo=data['cuerpo'])
            comentario.articulo = articulo
            comentario.autor = request.user
            comentario.save()
            return redirect(reverse('listar_blog'))
    else:
        formulario = ComentarioFormulario()
        contexto = {
            'formulario': formulario,
            'articulo': articulo,
        }

    return render(request, "app_blog/comentario_form.html", contexto)

#editar comentario, eliminar comentario