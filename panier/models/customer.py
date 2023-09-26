from django.db import models
from datetime import datetime
# from django.utils import timezone
# from .user import User



class Custumer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    firstName = models.CharField(max_length = 150, null=True,blank=True)
    lastName = models.CharField(max_length = 150, null=True,blank=True)
    phone = models.CharField(max_length = 150, null=True, blank=True)
    email = models.CharField(max_length = 150, null=True, blank=True)
    adress = models.CharField(max_length=255, null=True)
    birthday = models.DateField(default=datetime.now)  # Champ de date de naissance
    archived = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.firstName} {self.lastName}"