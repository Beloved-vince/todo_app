from django import forms
from .models import User

class Credentials(forms.ModelForm):
    class META:
        model = User
        fields = '__all__'