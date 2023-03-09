from typing import Tuple

from .models import Categoria, Libro

def valida_categoria(categoria: Categoria) -> Tuple[bool, str, str]:
    """
    Valida la longitud de los campos.
    Es llamada antes de guardar o actualizar una categoría.
    Si alguna validación falla regresa una tupla con False, el nombre del campo
    y un mensaje de error, caso contrario regresa True y dos valores nulos
    """
    if len(categoria.nombre) < 2:
        return (
            False,
            'nombre',
            'El nombre debe tener por lo menos 2 carácteres'
        )

    return True, None, None



def valida_libro(libro: Libro) -> Tuple[bool, str, str]:
    """
    Valida la longitud de los campos.
    Es llamada antes de guardar o actualizar un libro.
    Si alguna validación falla regresa una tupla con False, el nombre del campo
    y un mensaje de error, caso contrario regresa True y dos valores nulos
    """
    if len(libro.titulo) < 2:
        return (
            False,
            'titulo',
            'El título debe tener por lo menos 2 carácteres'
        )

    if len(libro.autor) < 2:
        return (
            False,
            'autor',
            'El autor debe tener por lo menos 2 carácteres'
        )

    return True, None, None
