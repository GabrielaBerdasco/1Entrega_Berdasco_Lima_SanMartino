from django.shortcuts import render

def Inicio(request):
    return render(request,"app_sanatorio/base.html")
    
