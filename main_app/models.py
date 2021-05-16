from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

DOSENO = (
    ('F', 'First'),
    ('S', 'Second'),
)



class Vaccine(models.Model):
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=100)
 

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('vaccines_detail', kwargs={'pk': self.id})

class Patient(models.Model):
  name = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  phoneNo = models.TextField(max_length=250)
  address = models.TextField(max_length=250)
  cityState = models.TextField(max_length=250)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  vaccines = models.ManyToManyField(Vaccine)
  
  

  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('detail', kwargs={'patient_id': self.id})

  def dose_for_today(self):
    return self.dose_set.filter(date=date.today()).count() >= len(DOSENO)

class Dose(models.Model):
  date = models.DateField('dose date')
  doseno = models.CharField(
		max_length=1,
		choices=DOSENO,
		default=DOSENO[0][0]
  )
  
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)



  def __str__(self):
    return f"{self.get_doseno_display()} on {self.date}"

class Meta:
    ordering = ['-date']

  
class Photo(models.Model):
  url = models.CharField(max_length=200)
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for patient_id: {self.patient_id} @{self.url}"
