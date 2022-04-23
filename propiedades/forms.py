"""Forms de Propiedades App - Clientes interesados en propiedad"""
from datetime import date
from django import forms
from .models import ClienteComprador, Propiedad

class ClienteCompradorForm(forms.Form):
    """Cliente interesado en Comprar Form"""
    nombre = forms.CharField()
    correo = forms.CharField()
    telefono = forms.CharField()
    mensaje = forms.CharField()
    def clean(self):
        nombre = self.cleaned_data.get("nombre")
        correo = self.cleaned_data.get("correo")
        telefono = self.cleaned_data.get("telefono")
        mensaje = self.cleaned_data.get("mensaje")

        prop_exists = ClienteComprador.objects.filter(
            nombre = nombre,
            correo = correo,
            telefono = telefono,
            mensaje = mensaje

        ).exists()

        if prop_exists:
            raise forms.ValidationError("Este mensaje ya fue enviado anteriormente")

        return self.cleaned_data

    def save(self, propiedad_interes_id):
        cliente = ClienteComprador(propiedad_interes_id=propiedad_interes_id,**self.cleaned_data)
        return cliente.save()