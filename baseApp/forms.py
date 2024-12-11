from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Submit
from baseApp.models import Estado

# Estado
class EstadoForm(forms.ModelForm):
    class Meta:
        model = Estado
        fields = ["nombre", "modelo", "descripcion", "color"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "modelo": forms.Select(attrs={"class": "form-select"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "color": forms.TextInput(
                attrs={"type": "color", "class": "form-control form-control-color"}
            ),
        }
