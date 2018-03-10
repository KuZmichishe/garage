# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse
from .models import Sensor, TemperatureHistory
from django.core.serializers import serialize
from .forms import FiltersForm
from django.db.models import Q
from django.db.models.functions import TruncDay, TruncHour, TruncMinute, TruncMonth, ExtractHour
from django.db.models import Avg


def index(request):
    if request.method == 'POST':
        form = FiltersForm(request.POST)
        if form.is_valid():
            filter = Q(requested_date__gt=form.cleaned_data['date_from']) & Q(requested_date__lt=form.cleaned_data['date_to'])
    else:
        form = FiltersForm()
    sensors = Sensor.objects.filter(type=2)
    for i, sensor in enumerate(sensors):
        sensors[i].temp = TemperatureHistory.objects.filter(
            sensor_id=sensor.id,
        ).annotate(
            date=TruncDay('requested_date'),
        )
        if request.method == 'POST':
            sensors[i].temp = sensors[i].temp.filter(filter)
    return render(
        request,
        'sensor/index.html', {
            'sensors': sensors,
            'form': form
        }
    )
