from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from app_sanatorio import views



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('about/', views.nosotros, name = "nosotros"),
    path('consulta/', views.busquedaEspecialidad, name= "consulta"),
    path('buscar/', views.buscar, name = "buscar"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)