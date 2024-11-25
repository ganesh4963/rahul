from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
# Create your views here.
def sign_up(request):
    if request.method=='POST':
        user=request.POST['username']
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        email=request.POST['emailid']
        pwd1=request.POST['password1']
        cpwd2=request.POST['password2']
        if pwd1!=cpwd2:
            return render(request,'signup.html',{"error":"password Mismatched"})
        else:
            try:
                User.objects.get(username=user)
                return render(request,"signup.html",{"error:user already existed"})
            except User.DoesNotExist:
                User.objects.create_user(username=user,first_name=fname,last_name=lname,email=email,password=pwd1)
                # return render(request,"signup.html",{"error":"user created successfully"})
                messages.success(request,"user created sucessfully")
                return redirect("home")


    else:
        return render(request,"signup.html")


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['status']=True
            return redirect('welcome')
        else:
            return render(request,"login.html",{"error":"Invalid username or password"})
    else:
        return render(request,"login.html")
    
