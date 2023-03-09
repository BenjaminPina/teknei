from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Categoria, Libro


def index(request):
    return render(request, 'libros/index.html')


class CategoriasLista(ListView):
    model = Categoria
    paginate_by = 5
    template_name='libros/categoria_lista.html'


class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = ['nombre']
    success_message = 'Categoría registrada correctamente'
    template_name='libros/categoria_alta.html'

    def get_success_url(self):
        return reverse('categoria_lista')


class CategoriaDetalle(DetailView):
    model = Categoria
    template_name='libros/categoria_detalle.html'


class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    model = Categoria
    form = Categoria
    fields = ['nombre']
    success_message = 'Categoría actualizada correctamente'
    template_name='libros/categoria_editar.html'

    def get_success_url(self):
        return reverse('categoria_lista')


class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria
    success_message = 'Categoría eliminada correctamente'

    def get_success_url(self):
        return reverse('categoria_lista')


class LibrosLista(ListView):
    model = Libro
    template_name='libros/libro_lista.html'


class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    form = Libro
    fields = ['titulo', 'autor', 'portada', 'categorias']
    success_message = 'Libro registrado correctamente'
    template_name='libros/libro_alta.html'

    def get_success_url(self):
        return reverse('libro_lista')


class LibroDetalle(DetailView):
    model = Libro
    template_name='libros/libro_detalle.html'


class LibroActualizar(SuccessMessageMixin, UpdateView):
    model = Libro
    form = Libro
    fields = ['titulo', 'autor', 'portada', 'categorias']
    success_message = 'Libro actualizado correctamente'
    template_name='libros/libro_editar.html'

    def get_success_url(self):
        return reverse('libro_lista')


class LibroEliminar(SuccessMessageMixin, DeleteView):
    model = Libro
    success_message = 'Libro eliminado correctamente'

    def get_success_url(self):
        return reverse('libro_lista')
