from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        # register user
        return
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        # login user
        return       
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect(request, 'index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')