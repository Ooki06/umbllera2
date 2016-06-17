from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, RequestContext
import time,datetime
import calendar
from .models import Room,Genre,User,Order



def	index(request):
	return render(request,'umbrella_system/index.html')

def	date(request, dates):
    gdate = int(dates)
    year = gdate//100
    month = gdate%100
    day = calendar.monthcalendar(year, month)
    dayweek = datetime.date(year,1,1)

    calendar.setfirstweekday(calendar.SUNDAY)
    dt = datetime.datetime(year,month,1)
    dt = datetime.datetime.fromtimestamp(time.mktime((year, month+1, 1, 0, 0, 0, 0, 0, 0)))
    next_date = dict({'year':dt.year,'month':dt.month,})
    dt = datetime.datetime.fromtimestamp(time.mktime((year, month-1, 1, 0, 0, 0, 0, 0, 0)))
    last_date = dict({'year':dt.year,'month':dt.month,})

    cal = dict({'year':year,'month':month,'days':day,})
    contexts = dict({'cal':cal,'next_date':next_date,'last_date':last_date,'messages': Room.objects.all(),'Dayweek': dayweek.weekday(),})

    return HttpResponse(render(request,'umbrella_system/date.html',contexts))

def room(request):
    contexts = dict({'messages': Room.objects.all(),})

    return HttpResponse(render(request, 'umbrella_system/room.html', contexts))