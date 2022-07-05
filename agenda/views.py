from django.shortcuts import render
from django.http import HttpResponse
import calendar
# Create your views here.


def index(request):

    return render(request, 'agenda/agenda.html')


def schedule(request):
    horraire =  list(range(8, 19))    
    return render(request, 'agenda/schedule.html', {"horraire": horraire})
