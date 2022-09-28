from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_sanatorio.urls')),
    path('accounts/', include('app_cuentas.urls')),
    path('page/', include('app_blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
