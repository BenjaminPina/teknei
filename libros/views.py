from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .validaciones import valida_categoria, valida_libro
from .models import Categoria, Libro


def index(request):
    return render(request, 'libros/index.html')


class CategoriasLista(ListView):
    model = Categoria
    ordering = ['nombre']
    paginate_by = 5
    template_name='libros/categoria_lista.html'


class CategoriaCrear(SuccessMessageMixin, CreateView):
    model = Categoria
    form = Categoria
    fields = ['nombre']
    success_message = 'Categoría registrada correctamente'
    template_name='libros/categoria_alta.html'

    def form_valid(self, form):
        """
        Validar el formulario antes de guardar en base de datos
        """
        categoria: Categoria = form.instance

        es_valido, campo, mensaje = valida_categoria(categoria)

        if not es_valido:
            form.add_error(campo, mensaje)
            return self.form_invalid(form)

        return super().form_valid(form)

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

    def form_valid(self, form):
        """
        Validar el formulario antes de guardar en base de datos
        """
        categoria: Categoria = form.instance

        es_valido, campo, mensaje = valida_categoria(categoria)

        if not es_valido:
            form.add_error(campo, mensaje)
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('categoria_lista')


class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria
    success_message = 'Categoría eliminada correctamente'

    def get_success_url(self):
        return reverse('categoria_lista')


class LibrosLista(ListView):
    model = Libro
    ordering = ['titulo']
    paginate_by = 5
    template_name='libros/libro_lista.html'

    def get_queryset(self):
        # aplicar el filtro por categoría
        categoria = self.request.GET.get('categoria')
        if categoria:
            return Libro.objects.filter(categorias__nombre=categoria)

        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # obtener lista de categorías
        categorias = Categoria.objects.all().order_by('nombre')
        context['categorias'] = categorias
        # obtener categoría seleccionada actualmente
        categoria = self.request.GET.get('categoria')
        if categoria:
            context['categoria_actual'] = categoria
        else:
            context['categoria_actual'] = ''

        return context


class LibroCrear(SuccessMessageMixin, CreateView):
    model = Libro
    form = Libro
    fields = ['titulo', 'autor', 'portada', 'categorias']
    success_message = 'Libro registrado correctamente'
    template_name='libros/libro_alta.html'

    def form_valid(self, form):
        """
        Validar el formulario antes de guardar en base de datos
        """
        libro: Libro = form.instance

        es_valido, campo, mensaje = valida_libro(libro)

        if not es_valido:
            form.add_error(campo, mensaje)
            return self.form_invalid(form)

        return super().form_valid(form)

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

    def form_valid(self, form):
        """
        Validar el formulario antes de guardar en base de datos
        """
        libro: Libro = form.instance

        es_valido, campo, mensaje = valida_libro(libro)

        if not es_valido:
            form.add_error(campo, mensaje)
            return self.form_invalid(form)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('libro_lista')


class LibroEliminar(SuccessMessageMixin, DeleteView):
    model = Libro
    success_message = 'Libro eliminado correctamente'

    def get_success_url(self):
        return reverse('libro_lista')
