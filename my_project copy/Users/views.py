from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import CustomUser
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
    
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        user_obj = User.objects.create_user(user_name, email, password)
        assign_group_to_user(user_obj, role)
        user_name = request.POST['user_name']
        phone_number=request.POST['phone_number']


        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'email already exists!')
            return redirect('register')
        if len(password)<6:
            messages.info(request, 'password must be of length 6 at least')
            return redirect('register')
        else:
         
            user_obj = User.objects.create_user(user_name, email, password)
            user_obj.save()
            group = Group.objects.get(name=role)  # Ensure the group exists
            user_obj.groups.add(group)
            customuser = CustomUser.objects.create(user=user_obj, name=name, email=email, user_name=user_name, phone_number=phone_number)
            customuser.save()
          
            return HttpResponse("This is a sample HTTP response.")
        
    else:
        return render(request,'register.html')


#LOGIN 
def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('register')
        


        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('login')
        
        login(request , user)
        return HttpResponse("This is a sample HTTP response.")
        #return redirect('/')

    return render(request , 'login.html')
def assign_group_to_user(user, role_name):
    group, created = Group.objects.get_or_create(name=role_name)
    user.groups.add(group)