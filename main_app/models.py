from django.db import models
from django.urls import reverse
from datetime import date

DOSENO = (
    ('F', 'First'),
    ('S', 'Second'),
)


class SideEffect(models.Model):
  name = models.CharField(max_length=50)
  description = models.CharField(max_length=200)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('sideeffects_detail', kwargs={'pk': self.id})

class Patient(models.Model):
  name = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  phoneNo = models.TextField(max_length=250)
  address = models.TextField(max_length=250)
  cityState = models.TextField(max_length=250)
  

  def __str__(self):
    return self.name

class Dose(models.Model):
  date = models.DateField('dose date')
  doseno = models.CharField(
		max_length=1,
		choices=DOSENO,
		default=DOSENO[0][0]
  )
  
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

  def dose_for_today(self):
    return self.dose_set.filter(date=date.today()).count() >= len(DOSENO)

  def __str__(self):
    return f"{self.get_doseno_display()} on {self.date}"

  def get_absolute_url(self):
    return reverse('detail', kwargs={'patient_id': self.id})

