from django.db import models
from . import User, Order

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sender_notification' )
    # recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_notification')
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='order_notification')
    read = models.BooleanField(default=False)
    recieved_date = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(default=False)