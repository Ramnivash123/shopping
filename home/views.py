from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('/signin')
    return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_superuser:
                return redirect('/admin_dash')
            else:
                return redirect('/user_dash')
        return redirect('/signin')
    return render(request, 'signin.html')

@login_required
def admin_dash(request):
    usrs=User.objects.all()
    return render(request, 'admin_dash.html', context={'usrs':usrs})

@login_required
def user_dash(request):
    return render(request, 'user_dash.html')

@login_required
def signout(request):
    logout(request)
    return redirect('/signin')

@login_required
def edit(request, id):
    usr=User.objects.get(id=id)
    return render(request, 'edit.html', context={'usr':usr})

@login_required
def edited(request, id):
    username=request.POST['username']
    is_superuser=request.POST['is_superuser']
    usr=User.objects.filter(id=id).update(username=username, is_superuser=is_superuser)
    return redirect('/admin_dash')

@login_required
def delete(request, id):
    usr=User.objects.filter(id=id).delete()
    return redirect('/admin_dash')





