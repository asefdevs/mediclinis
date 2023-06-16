from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import UserLoginForm,UserRegisterForm

# Create your views here.
def login_page(request):
    context={
        'form': UserLoginForm(),
        
    }

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            context['error']='username is not good'
    return render(request,'login.html',context)
            
       
def register_page(request):
    context={
        'form':UserRegisterForm(),  
        }
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return redirect('home')
    return render(request,'register.html',context)

def logout_user(request):
    logout(request)
    return redirect('home')

def edit_profile(request):
    return render(request,'profile.html')