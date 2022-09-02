from django.shortcuts import render


def base(request) :
    return render(request,"app_sanatorio/base.html")

def inicio(request) :
    return render(request, "app_sanatorio/inicio.html")

def medicos(request) :
    return render(request, "app_sanatorio/medicos.html")

def pacientes(request) :
    return render(request, "app_sanatorio/pacientes.html")

def obras_sociales(request) :
    return render(request, "app_sanatorio/obras-sociales.html")