from django.urls import path
from app_sanatorio import views



urlpatterns = [
    path('',views.base),
    path('inicio/', views.inicio, name = "inicio"),
    path('consulta/', views.busquedaEspecialidad, name= "consulta"),
    path('buscar/', views.buscar, name = "buscar"),
    path('medicos/', views.medicos_formulario, name = "medicos"),
    path('pacientes/', views.crear_paciente, name = "pacientes"),
]
