from django.urls import path
from .views import home, yaratish,uzgartirish

urlpatterns = [
    path("", home , name='home'),
    path("yaratish/", yaratish, name="yaratish") ,
    path("edit/ <int:pk>/" , uzgartirish , name='uzgartirish'),
]
