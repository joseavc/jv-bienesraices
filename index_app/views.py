"""Vistas de Index app"""

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index_app/index.html")
