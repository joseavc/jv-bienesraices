"""Vistas de Index app"""

from django.shortcuts import render

# Create your views here.
def hola(request):
    return render(request, "index_app/index.html")
