from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from customuser.models import CustomUser,Counsellor
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        Profession = request.POST['Profession']
        Age = request.POST['Age']
        phone_number= request.POST['phone_number']
        country=request.POST['country']

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('register')
        if len(password)<6:
            messages.info(request, 'password must be of length 6 at least')
            return redirect('register')
        else:
            user_obj = User.objects.create_user(email, email, password)
            user_obj.save()
            customuser = CustomUser.objects.create(user = user_obj , name=name,Profession=Profession,email=email,Age=Age,phone_number=phone_number,country=country)
            customuser.save()
            return redirect('login')
        
    else:
        return render(request,'register.html')
    

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('register')
        


        user = authenticate(username = email , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')
        
        login(request , user)
        print('success')
        if Counsellor.objects.filter(email=email).exists():
            return redirect('counsellor_dashboard')
        if CustomUser.objects.filter(email=email).exists():
            return redirect('patient_dashboard')

    return render(request , 'login.html')
    

def logout_user(request):
    logout(request)
    print('logout success')
    return redirect('index')


@login_required
def patient_dashboard(request):
    return render(request,'patient_dashboard.html')

@login_required
def counsellor_dashboard(request):
    return render(request,'counsellor_dashboard.html')