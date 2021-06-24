from django.shortcuts import render
from django.http import HttpResponse

from .models import User

def index(req):
    return render(req, 'index.html')

def get_all(req):
    return render(req, 'all_data.html')

# def index(req):
#     return HttpResponse(User.objects.all())