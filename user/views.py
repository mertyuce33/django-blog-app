from django.shortcuts import render,redirect,get_object_or_404
from .forms import RegisterForm,LoginForm,ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth import login as contrib_login
from .models import Profile

# Create your views here.
def register(request):
    
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']

        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,'Kayıt işlemi gerçekleştirilmiştir.')
        return redirect('index')
        
        
            
    context={
            'form': form
        }

    return render(request,"register.html",context)
   
def loginUser(request):
    form=LoginForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request,'Başarıyla giriş yapıldı.')
            login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Kullanıcı adı veya parola hatalı.')
            return render(request,'login.html',context)
       
    if request.user.is_authenticated:
        messages.info(request,'Zaten giriş yaptınız')
        return redirect('index')
        
    else:
        return render(request,"login.html",context)
def logoutUser(request):
    logout(request)
    messages.success(request,'Başarıyla çıkış yapılmıştır.')
    return redirect('index')
def profileUser(request):
    profile=get_object_or_404(Profile)
    return render(request,'profile.html',{'profile':profile})
def addProfile(request):
    form=ProfileForm(request.POST or None, request.FILES or None)

    context={
        'form':form
    }
    if form.is_valid():
        form.save()
        messages.success(request,'Profil başarı ile kaydedilmiştir.')
        return redirect('index')
    return render(request,"addprofile.html",context)

def editProfile(request):
    profile=get_object_or_404(Profile)
    form=ProfileForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
        messages.success(request,'Profiliniz başarı ile güncellenmiştir.')
        return redirect('index')
    return render(request,'editprofile.html',{'form':form})