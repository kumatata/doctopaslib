from django.shortcuts import render
from django.http import HttpResponse
import calendar
# Create your views here.


def index(request):
    
    return render(request, 'agenda/agenda.html')
