from django.shortcuts import render

# Create your views here.
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from core.models import Muatan as muatan

class MuatanDayArchiveView(DayArchiveView):
    queryset = muatan.objects.all()
    date_field = "date_added"
    allow_future = True

class MuatanTodayArchiveView(TodayArchiveView):
    queryset = muatan.objects.all()
    date_field = "date_added"
    allow_future = True


