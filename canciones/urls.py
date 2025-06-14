from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_canciones, name='lista_canciones'),
    path('crear/', views.crear_cancion, name='crear_cancion'),
    path('detalle/<int:cancion_id>/', views.detalle_cancion, name='detalle_cancion'),
    path('editar/<int:cancion_id>/', views.editar_cancion, name='editar_cancion'),
    path('eliminar/<int:cancion_id>/', views.eliminar_cancion, name='eliminar_cancion'),
]