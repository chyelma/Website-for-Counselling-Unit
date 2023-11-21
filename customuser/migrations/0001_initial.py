# Generated by Django 4.1.7 on 2023-11-18 20:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('name', models.CharField(default='', max_length=255)),
                ('email', models.EmailField(default='', max_length=254, primary_key=True, serialize=False, unique=True)),
                ('Gender', models.CharField(blank=True, max_length=255, null=True)),
                ('Profession', models.CharField(blank=True, max_length=255, null=True)),
                ('Age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801########'. Up to 11 digits allowed.", regex='^\\+8801\\d{9}$')])),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
