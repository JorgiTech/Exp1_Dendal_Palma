from django.urls import path
from .views import index,nosotros,galeria,api,formulario
from .import views


urlpatterns = [
    path('', views.index, name='home'), 
    path('index/', index,name='index'),
    path('nosotros/', nosotros,name='nosotros'),
    path('galeria/', galeria,name='galeria'),
    path('api/', api,name='api'),
    path('formulario/', formulario,name='formulario'),
    path('productos/', views.productos, name='productos'),
    path('agregar/', views.agregar, name='agregar'),
    path('agregarsave', views.agregarsave, name='agregarsave'),
    path('productos/eliminar/<int:id>/', views.eliminar, name='eliminar'),

 #   path('eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('productos/actualizar/<int:id>/', views.actualizar, name='actualizar'),
    path('actualizarsave/<int:id>/', views.actualizarsave, name='actualizarsave')

]
