from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_sanatorio.urls')),
    path('accounts/', include('app_cuentas.urls')),
    path('page/', include('app_blog.urls')),
]
