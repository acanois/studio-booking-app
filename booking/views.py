from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import InputUserForm
from django.views import generic

from .models import User, StudioBooking

def index(request):
    context = {
        'user_list': User.objects.all(),
    }
    return render(request, 'booking_home.html', context=context)


def get_all(request):
    context = {'user_list': User.objects.all()}
    return render(request, 'booking_home.html', context=context)

def create_user(request):
    pass

def get_user(request):
    pass

def get_user_by_pk(request):
    user = get_object_or_404(User, pk=1)
    context = {'user': user}
    return render(request, 'booking_home.html', context=context)

def update_user(request):
    pass

def delete_user(request):
    pass

class UserListView(generic.ListView):
    model = User
    user_context_name = 'user_list'
    queryset = User.objects.filter(first_name__icontains='Fen')
    template_name = 'booking_home.html'

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'user_detail.html'