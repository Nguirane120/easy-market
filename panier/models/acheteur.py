from django.db import models
from .user import User

class Acheteur(User):
    vendeurId = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acheteurs_created')


    # def __str__(self):
    #     pass
