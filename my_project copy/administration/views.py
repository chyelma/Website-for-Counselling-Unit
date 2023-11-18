from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
########
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import render
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
#from post.models import AdoptionRequest,Missinginfo,AdoptionPost
from Users.models import CustomUser
from django.utils import timezone
# Helper function to check if user is a staff member

def is_staff_member(user):
    return user.is_authenticated and user.is_staff

def admin_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            # Optionally, add a message to inform user of failed login
            messages.error(request, 'Invalid login credentials or not an admin user.')
            return redirect('admin_login')
    
    return render(request, 'admin_login.html')

@user_passes_test(is_staff_member, login_url=reverse_lazy('admin_login'))
def admin_dashboard(request):
    # Pass any required context to the admin_dashboard template if needed
    context = {}
    return render(request, 'admin_dashboard.html', context)
