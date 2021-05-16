# Generated by Django 3.1.7 on 2021-05-16 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('dose', models.CharField(choices=[('F', 'First'), ('S', 'Second')], default='F', max_length=1)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.patient')),
            ],
        ),
    ]
