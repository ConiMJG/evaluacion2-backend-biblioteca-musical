from django.shortcuts import render, redirect
from .forms import CancionForm
from .models import Cancion
from django.shortcuts import get_object_or_404


def crear_cancion(request):
    if request.method == 'POST':
        form = CancionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_canciones')
    else:
        form = CancionForm()

    return render(request, 'canciones/crear_cancion.html', {'form': form})

def lista_canciones(request):
    canciones = Cancion.objects.all()
    return render(request, 'canciones/lista_canciones.html', {'canciones': canciones})

def detalle_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    return render(request, 'canciones/detalle_cancion.html', {'cancion': cancion})

def editar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    if request.method == 'POST':
        form = CancionForm(request.POST, instance=cancion)
        if form.is_valid():
            form.save()
            return redirect('detalle_cancion', cancion_id=cancion.id)
    else:
        form = CancionForm(instance=cancion)
    
    return render(request, 'canciones/editar_cancion.html', {'form': form, 'cancion': cancion})

def eliminar_cancion(request, cancion_id):
    cancion = get_object_or_404(Cancion, pk=cancion_id)
    if request.method == 'POST':
        cancion.delete()
        return redirect('lista_canciones')
    
    return render(request, 'canciones/confirmar_eliminar.html', {'cancion': cancion})