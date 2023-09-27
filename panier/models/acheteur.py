from django.db import models
from .user import User 
from .vendeur import Vendeur 

class Acheteur(User):
    vendeur_id = models.ForeignKey(Vendeur, on_delete=models.CASCADE, related_name='acheteurs_created')


    # def __str__(self):
    #     pass
