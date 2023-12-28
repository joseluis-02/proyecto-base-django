# Django
from django.shortcuts import render
from django.views.generic import (
    TemplateView
)
# Views 
class PruebaTemplateView(TemplateView):
    template_name = 'prueba/index.html'
