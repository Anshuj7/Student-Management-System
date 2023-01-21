# Generated by Django 4.1.5 on 2023-01-17 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_staffs_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('cell_no', models.IntegerField()),
                ('vehicle_no', models.CharField(max_length=100)),
                ('vehicle_type', models.CharField(max_length=100)),
                ('aadhar', models.ImageField(upload_to='media/driver_info')),
                ('dl', models.ImageField(upload_to='media/driver_info')),
                ('rc', models.ImageField(upload_to='media/driver_info')),
                ('puc', models.ImageField(upload_to='media/driver_info')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stud_Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_amount', models.IntegerField()),
                ('fee_type', models.CharField(max_length=100)),
                ('fee_ref', models.CharField(max_length=100)),
                ('fee_stat', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.students', unique=True)),
            ],
        ),
    ]