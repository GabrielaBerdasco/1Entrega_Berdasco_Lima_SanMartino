from django import forms
""" from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User """

class MedicoFormulario(forms.Form):

    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    especialidad = forms.CharField(max_length=80)
    email = forms.EmailField()

""" class CrearPaciente(forms.Form):

    nombre = forms.CharField(max_length=80)
    apellido = forms.CharField(max_length=80)
    fecha_nacimiento = forms.DateField()
    ciudad = forms.CharField(max_length=80)
    telefono = forms.IntegerField()
    email = forms.EmailField()
 """

""" class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2'] """