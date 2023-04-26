from django import forms

from django.contrib.auth import get_user_model
from django.views.generic import FormView
from rest_framework import status
from rest_framework.response import Response

from users.forms import CustomUserCreationForm


class UserFormView(FormView):
    template_name = 'users/register_form.html'
    form_class = CustomUserCreationForm
    success_url = '/'
    
    def form_valid(self, form):
        get_user_model().objects.create(**form.cleaned_data)
        return super().form_valid(form)
