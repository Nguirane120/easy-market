from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages





def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            user = authenticate(username=phone, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username or passwor is incoorect')

        context = {}
        return render(request, 'dashboard/auth/login.html', context)
    



def logOutUser(request):
    logout(request)
    return redirect('login')