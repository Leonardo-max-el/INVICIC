from django import forms
from .models import work, actaEntrega
from django.contrib.auth.forms import AuthenticationForm

class RegistroForm(forms.ModelForm):
    class Meta:
        model = work
        fields = ['name', 'correo', 'contraseña']
        widgets = {
            'contraseña': forms.PasswordInput(),
        }

    def clean_contraseña(self):
        contraseña = self.cleaned_data.get('contraseña')
        # Podemos agregar validaciones adicionales aquí
        return contraseña

class LoginForm(AuthenticationForm):
    username = forms.EmailField(label='Correo electrónico')
    

class ActaEntregaForm(forms.ModelForm):
    class Meta:
        model = actaEntrega
        fields = ['usuario', 'archivo_word']