from django.shortcuts import render

# Create your views here.
def hola(request):
    return render(request, "propiedades/list.html")