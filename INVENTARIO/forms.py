from django import forms
from .models import ActaEntrega

class ActaEntregaForm(forms.ModelForm):
    class Meta:
        model = ActaEntrega
        fields = ['archivo_pdf']