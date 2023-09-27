from django.db import models
from .vendeur import Vendeur

class Category(models.Model):
    categoryName = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=512,blank=True, null=True)
    images = models.FileField(upload_to='uploads/categoriy',null=True, blank=True)
    vendeurId = models.ForeignKey(Vendeur, on_delete=models.CASCADE, related_name='category')
    archived = models.BooleanField(default=False)


    def __str__(self):
        return self.categoryName
