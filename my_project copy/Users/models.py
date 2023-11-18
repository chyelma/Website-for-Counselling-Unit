# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='')
    email = models.EmailField(primary_key=True, unique=True, default='')
    #role = models.CharField(max_length=255, default='')
    role = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    user_name = models.CharField(max_length=255, default='')
    phone_regex = RegexValidator(regex=r'^\+8801\d{9}$', message="Phone number must be entered in the format: '+8801########'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list

    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return self.name