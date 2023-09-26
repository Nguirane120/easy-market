from django.db import models 
# # from .user import User

# class Payment(models.Model):
#     paymentName = models.CharField(max_length=250, blank=True, null=True)
#     archived = models.BooleanField(default=False)


#     def __str__(self):
#         return self.paymentName
    
    
from django.contrib.postgres.fields import JSONField


class CallbackPayment(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.JSONField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.created_at