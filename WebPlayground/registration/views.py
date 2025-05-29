from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms


class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self) -> str:
        return reverse_lazy('login') + '?register'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-8', 'placeholder': 'Nombre de usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control mb-8', 'placeholder': 'Correo electrónico'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-10', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control mb-10', 'placeholder': 'Repite la Contraseña'}) 
        return form

