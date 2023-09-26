from django.contrib import admin
from .models import *
from .models.notification import Notification

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Custumer)
admin.site.register(CallbackPayment)
admin.site.register(Order)
admin.site.register(Panier)
admin.site.register(PanierElement)
admin.site.register(Notification)
admin.site.register(Image)
admin.site.register(Acheteur)
admin.site.register(Vendeur)

