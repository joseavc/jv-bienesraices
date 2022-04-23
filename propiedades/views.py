from typing import Type
from django.shortcuts import render, get_object_or_404, redirect
from .models import Propiedad, ClienteComprador
from .forms import ClienteCompradorForm
# Create your views here.
def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, "propiedades/propiedades.html", {"propiedades": propiedades})

def ver_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad,pk=pk)
    form = ClienteCompradorForm()
    
    if request.method == 'POST':
        form = ClienteCompradorForm(request.POST)
        if form.is_valid():
            form.save()

            

            return redirect("contacto:enviado")
    return render(request, "propiedades/detalle.html", {"propiedad": propiedad})
