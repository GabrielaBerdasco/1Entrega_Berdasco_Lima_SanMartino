from django.shortcuts import render


def inicio(request):
    return render(request,"app_sanatorio/base.html")
    
