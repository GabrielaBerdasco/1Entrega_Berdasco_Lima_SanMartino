from django.urls import path
from app_sanatorio import views
from app_sanatorio.views import Inicio


urlpatterns = [
    path("inicio/",Inicio),
]
