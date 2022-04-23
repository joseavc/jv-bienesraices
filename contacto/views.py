"""
View's de Contacto App
"""
from django.shortcuts import render, get_list_or_404, redirect
from django.views import generic as generic_views

from .forms import ClienteForm
from .models import Cliente

# Create your views here.
def crear_cliente(request):
    form = ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacto:enviado")
    return render(request, "contacto/contacto.html")

def confirmacion(request):
    return render(request, "captacion/confirmacion.html")
