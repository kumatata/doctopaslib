from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Prestations, Reservations, Specialites
from django.contrib.auth.decorators import user_passes_test, login_required



def home(self):
    specialities = Specialites.objects.all()
    return render(self, 'home/index.html', {'specialities': specialities})

def prestations(request,pk):
    prestations = Prestations.objects.filter(specialite__id=pk)
    return render(request, 'home/prestations.html', {'prestations': prestations})


def is_praticien(user):
     return Specialites.objects.filter(praticien__id=user.id).exists()

def is_patient(user):
    if is_praticien(user) == False:
     return True

@user_passes_test(is_patient)
@login_required
def reservations_patient(request):
    reservations = Reservations.objects.filter(patient__id=request.user.id)
    return render(request, 'patient/gestion.html', {'reservations': reservations})
