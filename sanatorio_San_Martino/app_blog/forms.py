from django import forms
from app_blog.models import Comentario


class ComentarioFormulario(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['cuerpo']