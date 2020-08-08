from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,"index.html")
        else:
            messages.error(request,'Wrong Credentials')
            return redirect('index')
    else:
        return render(request,'index.html')
       

def signup(request):
    
    if request.method == 'POST':
        fname = request.POST['f-name']
        sname = request.POST['s-name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        print(User.objects.filter(email=email).first())
        system_messages = messages.get_messages(request)
        if User.objects.filter(username=username).first() == None :
            if User.objects.filter(email=email).first() == None :    
                if pass1==pass2 :
                    user = User.objects.create_user(username=username,first_name = fname, last_name = sname,password=pass1,email=email)
                    user.save()            
                    print('user created')
                    login(request,user)
                    return render(request,'index.html')
                else:
                    
                    for msg in system_messages:
                        pass
                    print("password")
                    messages.error(request,'password did not match')
                    return render(request,'signup.html')
            else:
                for msg in system_messages:
                    del msg
                print("exist EMAIL")
                messages.error(request,'Account for this email has already created.Please use another email')
                return render(request,'signup.html')
        else:
            for msg in system_messages:
                    del msg
            print("exist ENO")
            messages.error(request,'An account for this Enrollment has already be made')
            return render(request,'signup.html')
    else:
        return render(request,'signup.html')  

def logged(request):
    logout(request)
    return redirect('index')        