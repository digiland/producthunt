from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    if request.method=='POST':
        if request.POST['password1']== request.POST['password2']:
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'passwords do no match'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #todo Need to add  route to homepage #TODO
    #TODO don't forget to logout
    return render(request, 'accounts/signup.html')