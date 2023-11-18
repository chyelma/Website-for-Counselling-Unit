from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse
from .models import Appointment
from Users.models import User
from Users.models import CustomUser
from django.contrib.auth.decorators import login_required
from datetime import datetime


def view_counselor_availability(request):
    available_counselors = User.objects.filter(role__name='Counselor', is_available=True)
    return render(request, 'counselor_availability.html', {'counselors': available_counselors}) #HTML

@login_required
def create_appointment(request):
    if request.method == 'POST':
        counselor_id = request.POST.get('counselor_id')
        date_time_str = request.POST.get('date_time')  # Expecting a string in the format 'YYYY-MM-DD HH:MM'

        try:
            counselor = CustomUser.objects.get(id=counselor_id)
            date_time = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M')
            appointment = Appointment.objects.create(
                patient=request.user,
                counselor=counselor,
                date_time=date_time,
                status='pending'  # or 'scheduled' based on your logic
            )
            # Redirect to a success page or appointment list
            return redirect('some_success_url')  
        except CustomUser.DoesNotExist:
            # Handle the error if the counselor does not exist
            return HttpResponse("Counselor not found.", status=404)

    # Assuming you have a list of counselors to choose from
    counselors = CustomUser.objects.filter(role='Counselor')
    return render(request, 'create_appointment.html', {'counselors': counselors})

def request_appointment(request):
    if request.method == 'POST':
        counselor_id = request.POST['counselor']
        date = request.POST['date']
        time = request.POST['time']
        datetime_str = f'{date} {time}'
        datetime_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M')

        counselor = CustomUser.objects.get(id=counselor_id)
        appointment = Appointment.objects.create(
            user_id=request.user,
            counselor=counselor,
            date_time=datetime_obj,
            status='pending'
        )
        return redirect('appointment_success')  # Redirect to a success page or dashboard

    counselors = CustomUser.objects.filter(role__name='Counselor')
    return render(request, 'request_appointment.html', {'counselors': counselors})

def approve_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if appointment.status != 'booked':
        appointment.status = 'scheduled'
        appointment.save()
        return HttpResponse("Appointment Approved")
    else:
        return HttpResponse("Appointment Already Booked")
def user_dashboard(request):
    available_appointments = Appointment.objects.filter(is_approved=True, status='scheduled')
    context = {
        'appointments': available_appointments
    }
    return render(request, 'user_dashboard.html', context)


def cancel_appointment(request, appointment_id):
    if request.method == 'POST':
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.status = 'cancelled'
        appointment.save()
        return HttpResponseRedirect('/appointments/')  # Redirect to the appointments page

    return render(request, 'cancel_appointment.html', {'appointment_id': appointment_id})

# Add other views as needed

