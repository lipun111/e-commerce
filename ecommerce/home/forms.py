from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PlaceholderMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field_names = [field_name for field_name, _ in self.fields.items()]
        for field_name in field_names:
            field = self.fields.get(field_name)
            field.widget.attrs.update({'placeholder': field.label})

class ContactForm(PlaceholderMixin,forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class UserRegistrationForm(PlaceholderMixin, UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name','last_name','username', 'email', ]

class GuestForm(PlaceholderMixin,forms.Form):
    email = forms.EmailField()

class LoginForm(PlaceholderMixin,forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
