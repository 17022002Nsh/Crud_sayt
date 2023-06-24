from django.db import models
from user.models import User


class Talim(models.Model):
    Ism_Familiya=models.CharField(max_length=100)
    Vaqti=models.DateTimeField(auto_now_add=True)
    done_at=models.DateTimeField(blank=True , null=True)
    Tekshiruvchi=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.SET_NULL, null=True ,blank=True)
    
