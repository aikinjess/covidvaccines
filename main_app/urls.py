from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('patients/', views.patients_index, name='index'),
  path('patients/<int:patient_id>/', views.patients_detail, name='detail'),
  path('patients/create/', views.PatientCreate.as_view(), name='patients_create'),
  path('patients/<int:pk>/update/', views.PatientUpdate.as_view(), name='patients_update'),
  path('patients/<int:pk>/delete/', views.PatientDelete.as_view(), name='patients_delete'),
  path('patients/<int:patient_id>/add_dose/', views.add_dose, name='add_dose'),
  path('vaccines/<int:pk>/', views.VaccineDetail.as_view(), name='vaccines_detail'),
  path('vaccines/create/', views.VaccineCreate.as_view(), name='vaccines_create'),
  path('vaccines/<int:pk>/update/', views.VaccineUpdate.as_view(), name='vaccines_update'),
  path('vaccines/<int:pk>/delete/', views.VaccineDelete.as_view(), name='vaccines_delete'),
  path('vaccines/', views.VaccineList.as_view(), name='vaccines_index'),
  path('patients/<int:patient_id>/assoc_vaccine/<int:vaccine_id>/', views.assoc_vaccine, name='assoc_vaccine'),
  path('accounts/signup/', views.signup, name='signup'),
  path('patients/<int:patient_id>/add_photo/', views.add_photo, name='add_photo')
]

