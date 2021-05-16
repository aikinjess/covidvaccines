from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Patient, SideEffect
from .forms import DoseForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def patients_index(request):
  patients = Patient.objects.all()
  return render(request, 'patients/index.html', { 'patients': patients })

def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  # instantiate FeedingForm to be rendered in the template
  dose_form = DoseForm()
  return render(request, 'patients/detail.html', {
    # include the cat and feeding_form in the context
    'patient': patient, 'dose_form': dose_form
  })

def add_dose(request, patient_id):
  form = DoseForm(request.POST)
  if form.is_valid():
    new_dose = form.save(commit=False)
    new_dose.patient_id = patient_id
    new_dose.save()
  return redirect('detail', patient_id=patient_id)

class PatientCreate(CreateView):
  model = Patient
  fields = '__all__'
  success_url = '/patients/'

class PatientUpdate(UpdateView):
  model = Patient
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['name', 'dob', 'phoneNo', 'address', 'cityState']

class PatientDelete(DeleteView):
  model = Patient
  success_url = '/patients/'


class SideEffectList(ListView):
  model = SideEffect

class SideEffectDetail(DetailView):
  model = SideEffect

class SideEffectCreate(CreateView):
  model = SideEffect
  fields = '__all__'

class SideEffectUpdate(UpdateView):
  model = SideEffect
  fields = ['name', 'description']

class SideEffectDelete(DeleteView):
  model = SideEffect
  success_url = '/sideeffects/'