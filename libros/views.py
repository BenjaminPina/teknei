from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin


from .models import Categoria, Libro


def index(request):
    return render(request, 'libros/index.html')


class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = ['nombre']
    success_message = 'Categoría registrada correctamente'

    def get_success_url(self):
        return reverse('index')


class CategoriasLista(ListView):
    model = Categoria
