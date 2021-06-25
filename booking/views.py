from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import InputUserForm

from .models import User, StudioBooking

def index(request):
    num_users = User.objects.all().count()
    num_bookings = StudioBooking.objects.all().count()

    context = {
        'num_users': num_users,
        'num_bookings': num_bookings
    }

    return render(request, 'booking_home.html', context=context)

# def get_all(req):
#     return render(req, 'all_data.html')

def new_user(req):
    # new_user = User()

    # new_user.first_name = 'Fenriz'
    # new_user.last_name = 'Fenriz'
    # new_user.band_name = 'Darkthrone'
    # new_user.save()

    # print(new_user)

    return render(req, 'createduser.html')
    # if req.method == 'POST':
    #     form = InputUserForm(req.POST)

        # if form.is_valid():
        #     return HttpResponse(req.body)


def get_all(req):
    print(User.objects.all())
    return HttpResponse(User.objects.all())