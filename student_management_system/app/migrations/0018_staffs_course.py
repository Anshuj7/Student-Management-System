# Generated by Django 4.1.5 on 2023-01-17 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.courses'),
        ),
    ]
