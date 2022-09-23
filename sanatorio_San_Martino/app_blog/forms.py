from django import forms
from app_blog.models import Comentario, Blog

class ComentarioFormulario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['cuerpo']


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']