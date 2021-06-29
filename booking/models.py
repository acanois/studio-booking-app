from django.db import models
from django.utils import timezone

"""Notes to self about how django handles sql:
    1. IDs as PKs are created automatically
    2. You have to run makemigration on the app name to create the the migration,
        and then run migrate to actually migrate the changes to the database
"""
    
class StudioBooking(models.Model):
    start_date = models.DateTimeField('start date', default=timezone.now)
    end_date = models.DateTimeField('end date', default=timezone.now)
    engineer = models.CharField(max_length=40)
    studio = models.CharField(max_length=20)
    cost_per_hour = models.FloatField()
    est_total_cost = models.FloatField()
