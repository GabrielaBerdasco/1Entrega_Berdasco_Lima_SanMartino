from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from app_cuentas import views



urlpatterns = [
    path('signup/', views.register, name = 'registro'),
    path('login/', views.login_request, name = 'login'),
    path('logout/', views.CustomLogoutView.as_view(), name = 'logout'),
    path('update-profile', views.editar_perfil, name = 'update_profile'),
    path('avatar', views.avatar_perfil, name = 'avatar')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)