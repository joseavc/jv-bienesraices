"""Forms de la app captacion"""
from dataclasses import field, fields
from datetime import date
from django import forms
from .models import Prospecto

class ProspectoForm(forms.Form):
    """Prospecto Form"""
    nombre_dueno = forms.CharField()
    municipio = forms.CharField()
    colonia = forms.CharField()
    estado = forms.CharField()
    tipo_credito = forms.CharField()
    saldo = forms.CharField(required=False)
    nss = forms.IntegerField(required=False)
    whatsapp = forms.CharField()

    def clean(self):
        nombre_dueno = self.cleaned_data.get("nombre_dueno")
        municipio = self.cleaned_data.get("municipio")
        colonia = self.cleaned_data.get("colonia")
        estado = self.cleaned_data.get("estado")
        tipo_credito = self.cleaned_data.get("tipo_credito")
        saldo = self.cleaned_data.get("saldo")
        nss = self.cleaned_data.get("nss")
        whatsapp = self.cleaned_data.get("whatsapp")

        prop_exists = Prospecto.objects.filter(
            nombre_dueno = nombre_dueno,
            municipio = municipio,
            colonia = colonia,
            whatsapp = whatsapp
        ).exists()

        if prop_exists:
            raise forms.ValidationError("Esta Prospecto ya esta registrada como prospecto")

        return self.cleaned_data

    def save(self):
        prospecto = Prospecto(**self.cleaned_data)
        return prospecto.save()