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
        views.CategoriasLista.as_view(),
         name='categoria_lista',
    ),
    path(
        'categorias/alta',
        views.CategoriaCrear.as_view(),
        name='categoria_alta',
    ),
    path(
        'categorias/detalle/<int:pk>',
        views.CategoriaDetalle.as_view(),
        name='categoria_detalle',
    ),
    path(
        'categorias/editar/<int:pk>',
        views.CategoriaActualizar.as_view(),
        name='categoria_editar',
    ),
    path(
        'categorias/eliminar/<int:pk>',
        views.CategoriaEliminar.as_view(),
        name='categoria_eliminar',
    ),
    path(
        'libros/lista',
        views.LibrosLista.as_view(),
        name='libro_lista',
    ),
    path(
        'libros/alta',
        views.LibroCrear.as_view(),
        name='libro_alta',
    ),
    path(
        'libros/detalle/<int:pk>',
        views.LibroDetalle.as_view(),
        name='libro_detalle',
    ),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
