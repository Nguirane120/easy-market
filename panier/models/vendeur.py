from django.db import models
from .user import User

class Vendeur(User):
    raisonSocial = models.CharField(max_length=250,blank=True, null=True)
    logo = models.ImageField(upload_to='images/logo/',null=True, blank=True)
    region = models.CharField(max_length=250,blank=True, null=True)
    ville = models.CharField(max_length=250,blank=True, null=True)
    
      
