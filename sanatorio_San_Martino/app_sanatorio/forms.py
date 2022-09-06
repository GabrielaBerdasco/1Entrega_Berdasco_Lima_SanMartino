from django import forms


class MedicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    especialidad = forms.CharField(max_length=80)
    email = forms.EmailField()

class CrearPaciente(forms.Form):

    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    fecha_nacimiento = forms.DateField()
    ciudad = forms.CharField(max_length=80)
    telefono = forms.IntegerField()
    email = forms.EmailField()

class ObrasFormulario(forms.Form):
    
    nombre = forms.CharField(max_length=80)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    
