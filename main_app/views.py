from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Patient
from .forms import DoseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def patients_index(request):
  patients = Patient.objects.filter(user=request.user)
  # You could also retrieve the logged in user's cats like this
  # cats = request.user.cat_set.all()
  return render(request, 'patients/index.html', { 'patients': patients })

@login_required
def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  dose_form = DoseForm()
  return render(request, 'patients/detail.html', {
    # include the cat and feeding_form in the context
    'patient': patient, 'dose_form': dose_form
  })

@login_required
def add_dose(request, patient_id):
  form = DoseForm(request.POST)
  if form.is_valid():
    new_dose = form.save(commit=False)
    new_dose.patient_id = patient_id
    new_dose.save()
  return redirect('detail', patient_id=patient_id)


class PatientCreate(LoginRequiredMixin,CreateView):
  model = Patient
  fields = '__all__'
  success_url = '/patients/'

@login_required
def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)


class PatientUpdate(LoginRequiredMixin,UpdateView):
  model = Patient
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'dob', 'phoneNo', 'address', 'cityState']

class PatientDelete(LoginRequiredMixin,DeleteView):
  model = Patient
  success_url = '/patients/'


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

