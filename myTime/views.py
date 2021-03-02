from django.shortcuts import render
from myTime.models import Location, DailyHours, Reservation, Report, WEEKDAYS
# from django.db.models import Q

from enum import Enum


# HOME Views

def home(request):
  context = {}
  return render(request, 'myTime/index.html', context)

def gymHome(request):
  context = {
    'pageName': 'CMU Weight Room',
    'pageToken': 'gym',
    'hours': '9-5pm',
    'capacity': 'Open'
  }
  return render(request, 'myTime/status.html', context)

def weigandHome(request):
  context = {
    'pageName': 'CMU Weigand Gymnasium',
    'pageToken': 'weigand',
    'hours': '9-5pm',
    'capacity': 'Open'
  }
  return render(request, 'myTime/status.html', context)


# GENERIC ACTIONS for Views

def reserveTimeslot(request):
  context={}

  if request.method == 'POST' and 'pageToken' in request.POST:
    loc = Location.objects.filter(token=request.POST['pageToken']).first()
    context['location'] = loc 
    context['weekdays'] = WEEKDAYS

    if 'timeslot' in request.POST:
      pass
      # reserve the timeslot

    return render(request, 'myTime/reserve.html', context)
    
  return render(request, 'myTime/index.html', context)

def reportCapacity(request):
  context = {}

  if request.method == 'POST' and 'pageToken' in request.POST:

    loc = Location.objects.filter(token=request.POST['pageToken']).first()
    context['location'] = loc 

    if 'capacity' in request.POST:
      pass
      # set the capacity 

    return render(request, 'myTime/report.html', context)

  return render(request, 'myTime/index.html', context)
