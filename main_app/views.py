from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def patients_index(request):
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