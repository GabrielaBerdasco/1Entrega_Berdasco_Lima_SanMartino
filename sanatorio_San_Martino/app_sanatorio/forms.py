from django import forms


class MedicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    especialidad = forms.CharField(max_length=80)
    email = forms.EmailField()

