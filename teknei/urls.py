from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from libros import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(
        'categorias/lista',
        views.CategoriasLista.as_view(template_name='libros/categoria_lista.html'),
        name='categoria_lista',
    ),
    path(
        'categorias/alta',
        views.CategoriaCrear.as_view(template_name='libros/categoria_alta.html'),
        name='categoria_alta',
    ),
    path(
        'categorias/detalle/<int:pk>',
        views.CategoriaDetalle.as_view(template_name='libros/categoria_detalle.html'),
        name='categoria_detalle',
    ),
    path(
        'libros/lista',
        views.LibrosLista.as_view(template_name='libros/libro_lista.html'),
        name='libro_lista',
    ),
    path(
        'libros/alta',
        views.LibroCrear.as_view(template_name='libros/libro_alta.html'),
        name='libro_alta',
    ),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
