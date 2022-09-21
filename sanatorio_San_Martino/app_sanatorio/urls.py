from django.urls import path
from app_sanatorio import views
from django.conf.urls import include



urlpatterns = [
    path('', views.inicio, name = "inicio"),
    path('about/', views.nosotros, name = "nosotros"),
    path('consulta/', views.busquedaEspecialidad, name= "consulta"),
    path('buscar/', views.buscar, name = "buscar"),
    path('crear-blog/', views.BlogCreateView.as_view(), name="crear_blog"),
    path('page/', views.BlogListView.as_view(), name = "listar_blog"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('page/page<int:id>/', views.ver_articulo, name="ver_articulo"),
]
