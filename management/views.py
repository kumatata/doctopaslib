from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Prestations, Specialites

    # template_name = 'home/index.html'
    # context_object_name = 'latest_specialities_list'

    # def get_queryset(self):
    #     return Specialites.objects.order_by('praticien')[:5]

def home(self):
    specialities = Specialites.objects.all()
    return render(self, 'home/index.html', {'specialities': specialities})

def prestations(request,pk):
    prestations = Prestations.objects.filter(specialite__id=pk)
    return render(request, 'home/prestations.html', {'prestations': prestations})
