from django.shortcuts import render


def index(request):
    return render(request, 'libros/index.html')
