from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms2 import LoginForm, EditForm



def user_login(request):
    if User.is_authenticated == True:
        return redirect('home_app: home')
   
    if request.method == 'POST':
        form =LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data.get('username'))
            login(request, user)
            return redirect('home_app:home')
    else:
        form = LoginForm()
    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         user = User.objects.get(username=form.cleaned_data.get('username'))
    #         login(request, user)
    #         return redirect('home_app:index.html')
        
    # else:
    #     form = LoginForm()
    return render (request, 'account_app/login.html', {'form': form})
        
        
        
        # user=authenticate(request, username=username, password=password)
        # # print(user.first_name)
        # if user is not None:
        #     login(request, user)
        #     return redirect('home_app:home')
             
             
        



def user_logout(request):
    logout(request)
    return redirect("home_app:home")


def user_register(request):
    
    
    if request.user.is_authenticated == True:
        return redirect('/')
    
    if request.method == "POST":
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        email=request.POST.get('email')
        
        User.objects.create(first_name=first_name, password=password1, email=email)
        return redirect('/')
        
    return render(request, 'account_app/register.html', {})


def edit_user(request):
    # user = request.user
    # form = EditForm(instance=user)
    # if request.method == 'POST':
    #     form = EditForm(instance=user, data=request.POST)
        
    #     if form.is_valid():
    #         form.save()
           
            
    # return render(request, 'account_app/edit.html', context={'form': form})

    user = request.user
    form = EditForm(instance=user)
    if request.method == 'POST':
        form = EditForm(instance=user, data=request.POST)
        if form.is_valid():
            form.save()
    def hi():
        return "hello how are you my frinds"       
    var = {
        
        
        "test": [1,2,3]
        
        
    }
    return render(request, 'account_app/edit.html', {'form': form, 'var': var})
        
