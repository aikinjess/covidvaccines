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
  path('sideeffects/<int:pk>/', views.SideEffectDetail.as_view(), name='sideeffects_detail'),
  path('sideeffects/create/', views.SideEffectCreate.as_view(), name='sideeffects_create'),
  path('sideeffects/<int:pk>/update/', views.SideEffectUpdate.as_view(), name='sideeffects_update'),
  path('sideeffects/<int:pk>/delete/', views.SideEffectDelete.as_view(), name='sideeffects_delete'),
  path('sideeffects/', views.SideEffectList.as_view(), name='sideeffects_index'),
]

