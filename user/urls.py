from django.urls import path
from .views import custom_register, custom_login


urlpatterns = [
    path("register/", custom_register, name='register'),
    path("login/", custom_login, name='login')
]
