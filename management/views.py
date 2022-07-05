from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Prestations, Specialites


def home(self):
    specialities = Specialites.objects.all()
    return render(self, 'home/index.html', {'specialities': specialities})

def prestations(request,pk):
    prestations = Prestations.objects.filter(specialite__id=pk)
    return render(request, 'home/prestations.html', {'prestations': prestations})
