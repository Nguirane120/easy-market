from django.db import models
from .user import User

class Acheteur(User):
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acheteurs_created')
    # status = models.CharField(max_length=16, choices=User.STATUS, default=User.ACHETEUR)


    # def __str__(self):
    #     pass
