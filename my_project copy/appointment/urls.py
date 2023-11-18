# appointment/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_appointment/', views.create_appointment, name='create_appointment'),
    path('request_appointment/', views.request_appointment, name='request_appointment'),
    path('cancel_appointment/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('approve_appointment/<int:appointment_id>/', views.approve_appointment, name='approve_appointment'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    # ... other paths as necessary ...
]
