from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from panier.models import *
# Create your views here.



@login_required(login_url='login')
def home(request):
    articles = Article.objects.all().count()
    orders = Order.objects.all().count()
    customers =  Custumer.objects.all().count()
    users = User.objects.all().count()


    context = {"articles":articles, "orders":orders, "customers":customers, "users":users}
    return render(request, 'dashboard/dashboard.html', context)