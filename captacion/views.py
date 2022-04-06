"""Vistas de captacion app"""

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic as generic_views

from .forms import PropiedadForm, PropiedadModelForm
from .models import Propiedad

#Normal Form
def crear_prospecto(request):
    form = PropiedadForm()
    if request.method == 'POST':
        form = PropiedadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("captacion:enviado")
    return render(request, "captacion/prospecto.html")

def confirmacion(request):
    return render(request, "captacion/confirmacion.html")
