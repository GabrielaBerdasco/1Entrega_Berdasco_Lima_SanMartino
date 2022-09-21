from django.urls import path
from app_cuentas import views



urlpatterns = [
    path('signup/', views.register, name = "registro"),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
    
]