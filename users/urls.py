from django.urls import path

from users.views import UserView

urlpatterns = [
    path('register/', UserView.as_view(), name='user register'),

]
