from django.db import models


class Image(models.Model):
    image = models.ImageField(
        upload_to='uploads/article', null=True, blank=True)
    archived = models.BooleanField(default=False)
    # Autres champs ou relations liés à l'image si nécessaire 