# Generated by Django 3.1.7 on 2021-05-16 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_patient_sideeffects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='sideeffects',
        ),
    ]