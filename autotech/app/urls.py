from django.urls import path, include
from main import views as main_views  # Importa las vistas de la aplicación main

urlpatterns = [
    path('', main_views.index, name='home'),
    path('index/', main_views.index, name='index'),
    path('nosotros/', main_views.nosotros, name='nosotros'),
    path('galeria/', main_views.galeria, name='galeria'),
    path('api/', main_views.api, name='api'),
    path('formulario/', main_views.formulario, name='formulario'),
    path('productos/', main_views.productos, name='productos'),
    path('agregar/', main_views.agregar, name='agregar'),
    path('agregarsave/', main_views.agregarsave, name='agregarsave'),
    path('productos/eliminar/<int:id>/', main_views.eliminar, name='eliminar'),
    path('actualizar/<int:id>/', main_views.actualizar, name='actualizar'),
    path('actualizarsave/<int:id>/', main_views.actualizarsave, name='actualizarsave'),
    path('carrito/', main_views.carrito, name='carrito'),  # Asocia la URL 'carrito/' con la vista 'carrito' de la aplicación main
    path('carrito/add/<int:producto_id>/', main_views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/delete/<int:item_id>/', main_views.eliminar_del_carrito, name='eliminar_del_carrito'),
]