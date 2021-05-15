from django.db import models
from django.urls import reverse

class Patient(models.Model):
  name = models.CharField(max_length=100)
  dob = models.CharField(max_length=100)
  phoneNo = models.TextField(max_length=250)
  address = models.TextField(max_length=250)
  cityState = models.TextField(max_length=250)

  def __str__(self):
    return self.name
    
  # Add this method
  def get_absolute_url(self):
    return reverse('detail', kwargs={'patient_id': self.id})