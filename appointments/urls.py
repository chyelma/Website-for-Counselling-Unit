from django.urls import path
from .views import create_appointment,req_appointment,view_all_appointment,upcoming_appointment

urlpatterns = [
    path('create_appointment/', create_appointment , name='create_appointment'),
    path('upcoming_appointment/', upcoming_appointment, name='upcoming_appointment'),
    path('view_all_appointment/', view_all_appointment, name='view_all_appointment'),
    path('<int:pk>/request_appointment/', req_appointment, name='request_appointment'),  
]