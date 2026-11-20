from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from .forms import RegForm
from .models import Profile

# Create your views here.
# login
def loginpage(request):
    if request.method == 'POST':
        usern = request.POST.get("usern")
        passw = request.POST.get("passw")
        print(usern)
        print(passw)
        user =authenticate(request,username=usern,password=passw)
        if user:
            login(request,user)
            print(user)
            # return HttpResponse('hello')
        else:
            print('no such user')

    return render(request,'login.html')


# logout
def logoutpage(request):
    logout(request)
    # return HttpResponse('user logged out')
    return redirect(loginpage)




def registerpage(request):
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            usr= form.save()
            Profile.objects.create(user=usr)
            return redirect(loginpage)
    else:
        form = RegForm()
    return render(request,'register.html',{'form':form})

