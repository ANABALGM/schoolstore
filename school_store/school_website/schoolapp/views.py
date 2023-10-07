from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request,'Home.html')

def register(request):

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            cpassword = request.POST['password1']

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exits')
                    return redirect('schoolapp:register')

                else:
                    user = User.objects.create_user(username=username,password=password)

                    user.save();
                    return redirect('schoolapp:login')
            else:
                messages.info(request, 'password not matched')
                return redirect('schoolapp:register')
            return redirect('/')

        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/detail')
        else:

            messages.info(request, 'Invalid Username or Password')
            return redirect('schoolapp:login')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
def detail(request):
    return render(request,'detail.html')

