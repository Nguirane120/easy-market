from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .user import User

class Panier(models.Model):
    userId = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date_creation = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return f"Panier de {self.utilisateur.username}"
