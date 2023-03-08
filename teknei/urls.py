from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from libros import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path(
        'categorias/alta',
        views.CategoriaCrear.as_view(template_name='libros/categoria_alta.html'),
        name='categoria_alta',
    ),
    path(
        'categorias/lista',
        views.CategoriasLista.as_view(template_name='libros/categoria_lista.html'),
        name='categoria_lista',
    ),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
