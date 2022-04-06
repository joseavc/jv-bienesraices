"""Forms de la app captacion"""
from dataclasses import field, fields
from datetime import date
from django import forms
from .models import Propiedad

class PropiedadForm(forms.Form):
    """Propiedad Form"""
    nombre_dueno = forms.CharField()
    municipio = forms.CharField()
    estado = forms.Textarea
    tipo_credito = forms.CharField()
    saldo = forms.CharField(required=False)
    nss = forms.IntegerField(required=False)
    whatsapp = forms.IntegerField()

    def clean(self):
        nombre_dueno = self.cleaned_data.get("nombre_dueno")
        municipio = self.cleaned_data.get("municipio")
        estado = self.cleaned_data.get("estado")
        tipo_credito = self.cleaned_data.get("tipo_credito")
        saldo = self.cleaned_data.get("saldo")
        nss = self.cleaned_data.get("nss")
        whatsapp = self.cleaned_data.get("whatsapp")

        prop_exists = Propiedad.objects.filter(
            nombre_dueno = nombre_dueno,
            municipio = municipio,
            whatsapp = whatsapp
        ).exists()

        if prop_exists:
            raise forms.ValidationError("Esta propiedad ya esta registrada como prospecto")

        return self.cleaned_data

    def save(self):
        propiedad = Propiedad(**self.cleaned_data)
        return propiedad.save()


class PropiedadModelForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'

    def clean(self):
        nombre_dueno = self.cleaned_data.get("nombre_dueno")
        municipio = self.cleaned_data.get("municipio")
        estado = self.cleaned_data.get("estado")
        tipo_credito = self.cleaned_data.get("tipo_credito")
        saldo = self.cleaned_data.get("saldo")
        nss = self.cleaned_data.get("nss")
        whatsapp = self.cleaned_data.get("whatsapp")

        prop_exists = Propiedad.objects.filter(
            nombre_dueno = nombre_dueno,
            municipio = municipio,
            whatsapp = whatsapp
        ).exists()

        if prop_exists:
            raise forms.ValidationError("Esta propiedad ya esta registrada como prospecto")

        return self.cleaned_data 
