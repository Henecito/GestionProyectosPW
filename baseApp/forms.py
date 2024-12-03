from django import forms
from baseApp.models import Estado

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["nombre"]
        widgets = {"nombre": forms.TextInput(attrs={"class": "form-control"})}

