from django.db import models

# Create your models here.


from django.db import models
# from .user import User

class Category(models.Model):
    categoryName = models.CharField(max_length=250, blank=True, null=True)
    description = models.CharField(max_length=512,blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='category')
    archived = models.BooleanField(default=False)


    def __str__(self):
        return self.categoryName
