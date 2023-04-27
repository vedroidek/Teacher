from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser


class CustomUserCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = get_user_model().objects.exclude(is_superuser=True)

    email = forms.EmailField(min_length=10, label='e-mail address', required=True,
                             widget=forms.EmailInput)
    username = forms.CharField(max_length=150, min_length=3, required=True,
                               error_messages={"required": "Please enter your username"},
                               label='username')
    user_type = forms.ChoiceField(choices=CustomUser.USER_STATUS_CHOICES, label='user type',
                                  widget=forms.Select,
                                  error_messages={"required": "Please enter user type"})
    password = forms.CharField(label='password', widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='password_confirm', widget=forms.PasswordInput())

    field_order = ('username', 'email', 'user_type', 'password', 'password_confirm')

    def clean(self):
        cleaned_data = super(get_user_model(), self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("password_confirm")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and password_does not match"
            )

    class Meta:
        model = get_user_model()
        exclude = ['is_staff', 'is_superuser', 'groups', 'user_permissions', 'last_login']
