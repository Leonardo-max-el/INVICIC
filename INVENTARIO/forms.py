from django import forms
from .models import actaEntrega

class ActaEntregaForm(forms.ModelForm):
    class Meta:
        model = actaEntrega
        fields = ['archivo_pdf']