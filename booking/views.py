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

# def index(request):
#     return render(request, 'booking_home.html')

# class UserListView(LoginRequiredMixin, generic.ListView):
#     model = User
#     user_context_name = 'user_list'
#     queryset = User.objects.all()
#     template_name = 'booking_home.html'

# class UserDetailView(LoginRequiredMixin, generic.DetailView):
#     model = User
#     template_name = 'user_detail.html'