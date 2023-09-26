from django.shortcuts import render, redirect
from panier.models import Order



def commandeList(request):
    orders = Order.objects.all()
    context = {"orders":orders}
    return render(request, 'dashboard/commandes/listCommandes.html', context)