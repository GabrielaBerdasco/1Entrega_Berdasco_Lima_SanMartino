from django.urls import path
from app_cuentas import views



urlpatterns = [
    path('signup/', views.register, name = "registro")
    
]
