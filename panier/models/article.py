from django.db import models
from .user import User
from .category import Category
from .images import Image


class Article(models.Model):
    articleName = models.CharField(max_length=250, blank=True, null=True)
    articleDescription = models.CharField(
        max_length=512, blank=True, null=True)
    articlePrice = models.FloatField()
    articleActif = models.BooleanField(default=False, blank=True, null=True)
    articleInStock = models.IntegerField()
    articleInStockSecurite = models.IntegerField(blank=True, null=True)
    categoryId = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    # images = models.FileField(
    #     upload_to='uploads/article', null=True, blank=True)
    images = models.ManyToManyField(Image, blank=True)
    userId = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, related_name='articles')
    archived = models.BooleanField(default=False)
    isFavorite = models.BooleanField(default=False)

    def __str__(self):
        return self.articleName
