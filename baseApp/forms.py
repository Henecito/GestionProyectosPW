from django import forms
from baseApp.models import Estado

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["nombre", "desc"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "desc": forms.Textarea(attrs={"class": "form-control", "row": 2})
            }

