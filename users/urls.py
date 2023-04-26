from django.urls import path

from users.views import UserFormView

urlpatterns = [
    path('register/', UserFormView.as_view(), name='user register'),
]
