from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

@login_required(login_url='login')
def Homepage(request):
    return render (request, 'home.html')

def RegisterPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')

        if not uname or not email or not password:
            return HttpResponse("Username, email, and password are required.")

        # Create the user
        try:
            my_user = User.objects.create_user(username=uname, email=email, password=password)
            my_user.save()

            profile = Profile(user=my_user, photo=photo)
            profile.save()
            return redirect('login')
        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    return render(request, 'register.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!")
    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')