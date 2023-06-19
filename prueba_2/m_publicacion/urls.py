from django.urls import path
from .views import (
    mostrar_notas,
    mostrar_nueva_publicacion
)
urlpatterns = [
    path('', mostrar_notas, name='mostrar_notas'),
    path('nueva/', mostrar_nueva_publicacion,name='mostrar_nueva_publicacion')
]