from django.urls import path
from app_sanatorio import views
from app_sanatorio.views import inicio



urlpatterns = [
    path('',views.base),
    path('inicio/', views.inicio, name = "inicio")
]
