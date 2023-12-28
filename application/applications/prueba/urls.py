# Rutas de la aplicación prueba
from django.urls import path
# my views
from .views import PruebaTemplateView
urlpatterns = [
    path(
        '',
        PruebaTemplateView.as_view(),
        name='index'
    ),
]