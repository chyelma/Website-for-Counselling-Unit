# Generated by Django 4.2.7 on 2023-11-17 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Users", "0003_add_missing_groups"),
        ("appointment", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="user_id",
        ),
        migrations.AlterField(
            model_name="appointment",
            name="counselor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="counselor_appointments",
                to="Users.customuser",
            ),
        ),
    ]
