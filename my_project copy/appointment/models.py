# appointment/models.py
from django.db import models
from django.contrib.auth.models import User
from Users.models import CustomUser

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_appointments')
    counselor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='counselor_appointments')
    date_time = models.DateTimeField()
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('pending', 'Pending Approval'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment {self.id} with {self.patient.username}"
