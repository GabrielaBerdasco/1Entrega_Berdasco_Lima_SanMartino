from django.urls import path
from app_sanatorio import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('consulta/', views.busquedaEspecialidad, name= "consulta"),
    path('buscar/', views.buscar, name = "buscar"),
]
