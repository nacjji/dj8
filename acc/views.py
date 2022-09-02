from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")


def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            return redirect("acc:index")
        else:
            pass # 마지막 날 메세지 추가
    return render(request, "acc/login.html")


def profile(request):
    return render(request,'acc/profile.html')

def signup(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        up=request.POST.get('upass')
        uc=request.POST.get('ucomment')
        up=request.FILES.get('upic')
        try:
            User.objects.create_user(username=un,password=up,comment=uc,pic=up)
            return redirect('acc:login')
        except:
            pass
    return render(request,'acc/signup.html')

def update(request):
    if request.method=="POST":
        u=request.user
        ue = request.POST.get("umail")
        uc = request.POST.get("ucomm")
        up = request.FILES.get("upic")
        u.email,u.comment=ue,uc
        if up:
            u.pic.delete()
            u.pic=up
        u.save()
        return redirect('acc:profile')
    return render(request,'acc/update.html') 
    
def delete(request):
    u=request.user
    cp=request.POST.get('cpass')
    if check_password(cp,u.password):
        np=request.POST.get('npass')
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    return redirect('acc:update')

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp,u.password):
        np=request.POST.get('npass')
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    return redirect('acc:update')