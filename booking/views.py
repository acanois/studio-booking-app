import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import InputUserForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from .models import StudioBooking

booking_home = never_cache(TemplateView.as_view(template_name='index.html'))

def submit_booking_data(req):
    if req.method == 'POST':
        body = json.loads(req.body.decode('utf-8'))
        new_booking = StudioBooking(
            first_name=body['firstName'],
            last_name=body['lastName'],
            band_name=body['bandName'],
            start_date=body['startDate'],
            end_date=body['endDate'],
            engineer=body['engineer'],
            studio=body['studio'],
            cost_per_hour=body['costPerHour'],
            est_total_cost=body['estTotalCost']
        )
        new_booking.save()
    return HttpResponse(req)