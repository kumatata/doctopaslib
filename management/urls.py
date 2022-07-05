from django.urls import path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('specialite/<int:pk>/', views.prestations, name='specialites'),
    path('mes-rendez-vous/', views.reservations_patient, name='gestion')
]
