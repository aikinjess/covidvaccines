from django.db import models
from django.urls import reverse

DOSENO = (
    ('F', 'First'),
    ('S', 'Second'),
)

class Patient(models.Model):
  name = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  phoneNo = models.TextField(max_length=250)
  address = models.TextField(max_length=250)
  cityState = models.TextField(max_length=250)

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
    


  def get_absolute_url(self):
    return reverse('detail', kwargs={'patient_id': self.id})