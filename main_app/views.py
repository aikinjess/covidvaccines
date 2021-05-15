from django.shortcuts import render
from .models import Patient
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def patients_index(request):
  patients = Patient.objects.all()
  return render(request, 'patients/index.html', { 'patients': patients })

class Patient:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, dob, phoneNo, address, cityState):
    self.name = name
    self.dob = dob
    self.phoneNo = phoneNo
    self.address = address
    self.cityState = cityState

patients = [
  Patient('Jessica', '07/05/1970', '989-678-7894', '456 Joy Rd', 'Detroit, MI'),
  Patient('Tamika Ray', '07/25/1990', '989-888-7894', '456 Terry Rd', 'Saginaw, MI'),
]