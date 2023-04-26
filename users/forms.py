from django import forms
from django.contrib.auth import get_user_model


class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'user_type']
