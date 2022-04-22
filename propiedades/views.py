from django.shortcuts import render, get_object_or_404
from .models import Propiedad

# Create your views here.
def lista_propiedades(request):
    propiedades = Propiedad.objects.all()
    return render(request, "propiedades/propiedades.html", {"propiedades": propiedades})

def ver_propiedad(request, pk):
    propiedad = get_object_or_404(Propiedad,pk=pk)

    return render(request, "propiedades/detalle.html", {"propiedad": propiedad})
