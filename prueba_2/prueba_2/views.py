# Copiar y pegar :D
from django.shortcuts import render, redirect

from .precios import precios
from .historial import historial
from .recuerdos import recuerdos

def mostrar_principal(request):
    return render(request,'principal.html')

def mostrar_precios(request):
    contexto = {
        'precios': precios
    }
    return render(request,'precios.html', contexto)

def mostrar_historial(request):
    contexto = {
        'historial': historial
    }
    return render(request,'historial.html',contexto)

def mostrar_recuerdos(request):
    contexto = {
        'recuerdos':recuerdos
    }
    return render(request,'recuerdos.html',contexto)
