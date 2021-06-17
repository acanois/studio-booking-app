from django.contrib import admin

# Register your models here.
from .models import User, StudioBooking

admin.site.register(User)
admin.site.register(StudioBooking)