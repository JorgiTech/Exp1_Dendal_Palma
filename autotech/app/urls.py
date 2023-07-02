from django.urls import path
from .views import index,nosotros,galeria,api,formulario


urlpatterns = [
    path('', index,name='index'),
    path('', nosotros,name='nosotros'),
    path('', galeria,name='galeria'),
    path('', api,name='api'),
    path('', formulario,name='formulario')
]
