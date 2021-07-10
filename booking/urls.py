from django.urls import path

# DO NOT KEEP THIS
from django.views.decorators.csrf import csrf_exempt

from . import views

"""TODO:
    Switch these to re_path as needed
"""
urlpatterns = [
    path('', views.booking_home, name='index'),
    path('submit-booking-data', csrf_exempt(views.submit_booking_data), name='index'),
]