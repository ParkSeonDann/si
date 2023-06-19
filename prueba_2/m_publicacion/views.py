from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioPublicacion
from sweetify import success, warning
from .models import ModeloPublicacion
# Create your views here.
@login_required # LOGIN_URL que esta en el settings y ahí se define el lugar
def mostrar_nueva_publicacion(request):
    if request.method == 'GET':
        contexto = {
            'formulario': FormularioPublicacion()
        }
        return render(request, 'notas/agregar.html',contexto)
    if request.method == 'POST':
        datos_pub = FormularioPublicacion(data = request.POST)
        if datos_pub.is_valid():
            pub_guardada = datos_pub.save(commit = False)
            pub_guardada.usuario = request.user
            pub_guardada.save()
            success(request, f'Publicación {pub_guardada.titulo} correctamente')
            return redirect('mostrar_notas')
        warning(request, 'Complete los campos con errores')
        contexto = {
            'formulario': datos_pub
        }
        return render(request, 'notas/agregar.html', contexto)

def mostrar_notas(request):
    todas_publicaciones = ModeloPublicacion.objects.all()
    contexto = {
        'publicaciones': todas_publicaciones
    }
    return render(request,'notas/listar.html', contexto)