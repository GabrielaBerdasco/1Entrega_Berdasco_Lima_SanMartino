from django.urls import path
from app_blog import views
from django.conf.urls import include



urlpatterns = [
    path('crear-blog/', views.BlogCreateView.as_view(), name="crear_blog"),
    path('', views.BlogListView.as_view(), name = "listar_blog"),
    path('page<int:id>/', views.ver_articulo, name="ver_articulo"),
    path('page<int:id>/comentario', views.comentario_form, name='comentario_form' ),
    path('eliminar-comentario/<int:pk>', views.ComentarioDeleteView.as_view(), name="eliminar_comentario"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('editar-blog/<int:pk>', views.BlogUpdateView.as_view(), name="editar_blog"),
    path('eliminar-blog/<int:pk>', views.BlogDeleteView.as_view(), name="eliminar_blog"),
]


