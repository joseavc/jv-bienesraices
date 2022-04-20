"""Forms de Contacto App"""
from datetime import date
from django import forms
from .models import Cliente

class ClienteForm(forms.Form):
    """Cliente Form"""
    nombre = forms.CharField()
    correo = forms.CharField()
    telefono = forms.CharField()
    interes = forms.CharField()
    mensaje = forms.CharField()

    def clean(self):
        nombre = self.cleaned_data.get("nombre")
        correo = self.cleaned_data.get("correo")
        telefono = self.cleaned_data.get("telefono")
        interes = self.cleaned_data.get("interes")
        mensaje = self.cleaned_data.get("mensaje")

        prop_exists = Cliente.objects.filter(
            nombre = nombre,
            correo = correo,
            mensaje = mensaje
        ).exists()

        if prop_exists:
            raise forms.ValidationError("Este mensaje ya fue enviado anteriormente")

        return self.cleaned_data

    def save(self):
        contacto = Cliente(**self.cleaned_data)
        return contacto.save()
    