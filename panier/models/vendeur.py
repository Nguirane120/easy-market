from django.db import models
from .user import User

class Vendeur(User):

    def __str__(self):
        return self.firstName
