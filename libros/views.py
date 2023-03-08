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


class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = ['nombre']
    success_message = 'Categoría registrada correctamente'

    def get_success_url(self):
        return reverse('index')


class CategoriaDetalle(DetailView):
    model = Categoria


class LibrosLista(ListView):
    model = Libro


class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    form = Libro
    fields = ['titulo', 'autor', 'portada', 'categorias']
    success_message = 'Libro registrado correctamente'

    def get_success_url(self):
        return reverse('index')
