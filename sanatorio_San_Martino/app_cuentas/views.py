from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from app_cuentas.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from app_cuentas.models import Avatar


def register(request):
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "app_sanatorio/inicio.html", {"mensaje": "Usuario Creado :)"})
        else:
            mensaje = 'Cometiste un error en el registro'
    formulario = UserRegisterForm()
    context = {
        'form': formulario,
        'mensaje': mensaje,
        'value': 'Registrarse'
    }

    return render(request, "app_cuentas/registro.html", context=context)


def login_request(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                return render(request, "app_sanatorio/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"app_sanatorio/inicio.html", {"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"app_sanatorio/inicio.html", {"mensaje":"Error, formulario erroneo"})

    form = AuthenticationForm()
    return render(request,"app_cuentas/login.html", {'form':form} )


class CustomLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'app_cuentas\logout.html'


def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        form = UserUpdateForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario.last_name = data['last_name']
            usuario.first_name = data['first_name']
            usuario.email = data['email']

            usuario.save()

            return redirect(reverse('inicio'))
    else:  
        inicial = {
            'last_name': usuario.last_name,
            'first_name': usuario.first_name,
            'email': usuario.email,
        }
        form = UserUpdateForm(initial=inicial)
        contexto = {
            "form": form,
            "value": "Confirmar cambios"
        }
    return render(request, "app_cuentas/registro.html", contexto)


def avatar_perfil(request):

    if request.method == 'POST':
        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid:
            avatar = form.save()
            avatar.usuario = request.user
            avatar.save()

            return redirect(reverse('inicio'))
    else:
        form = AvatarFormulario()

        return render(request, "app_cuentas/form_avatar.html", {"form":form})


def avatar_eliminar(request):
    avatar = Avatar.objects.get(usuario = request.user)
    avatar.delete()
    
    return redirect(reverse('avatar'))
