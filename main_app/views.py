from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Patient, Vaccine, Photo
from .forms import DoseForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'gethevax'
import uuid
import boto3
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def patients_index(request):
  patients = Patient.objects.filter(user=request.user)
  return render(request, 'patients/index.html', {'patients': patients})

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def patients_detail(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  vaccines_patient_doesnt_have = Vaccine.objects.exclude(id__in = patient.vaccines.all().values_list('id'))
  dose_form = DoseForm()
  return render(request, 'patients/detail.html', {'patient': patient, 'dose_form': dose_form, 'vaccines': vaccines_patient_doesnt_have})

class PatientCreate(LoginRequiredMixin, CreateView):
  model = Patient
  fields = ['name', 'dob', 'phoneNo', 'address', 'cityState']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PatientUpdate(LoginRequiredMixin, UpdateView):
  model = Patient
  fields = ['name', 'dob', 'phoneNo', 'address', 'cityState']


class PatientDelete(LoginRequiredMixin, DeleteView):
  model = Patient
  success_url = '/patients/'

@login_required
def add_dose(request, patient_id):
  form = DoseForm(request.POST)
  if form.is_valid():
    new_dose = form.save(commit=False)
    new_dose.patient_id = patient_id
    new_dose.save()
  return redirect('detail', patient_id=patient_id)

class VaccineList(ListView):
  model = Vaccine

class VaccineDetail(DetailView):
  model = Vaccine

class VaccineCreate(CreateView):
  model = Vaccine
  fields = '__all__'

class VaccineUpdate(UpdateView):
  model = Vaccine
  fields = ['name', 'location']

class VaccineDelete(DeleteView):
  model = Vaccine
  success_url = '/vaccines/'

@login_required
def assoc_vaccine(request, patient_id, vaccine_id):
  Patient.objects.get(id=patient_id).vaccines.add(vaccine_id)
  return redirect('detail', patient_id=patient_id)

def add_photo(request, patient_id):
  # photo-file will be the "name" attribute on the <input type="file">
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # need a unique "key" for S3 / needs image file extension too
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # just in case something goes wrong
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      # build the full url string
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # we can assign to cat_id or cat (if you have a cat object)
      photo = Photo(url=url, patient_id=patient_id)
      photo.save()
    except Exception as err:
      print('An error occurred uploading file to S3: %s' % err)
  return redirect('detail', patient_id=patient_id)

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
