from .models import Reger
from django.forms import ModelForm, PasswordInput

class RegerForm(ModelForm):
    class Meta:
        model = Reger
        fields = ['admin_password']

        widgets = {
            "admin_password": PasswordInput(attrs={
                'type': 'password',
                'class': 'register__input',
                'name': 'password',
                'id':'login_password',
            }),
        }
