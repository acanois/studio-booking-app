from django.db import models
from django.utils import timezone

"""Notes to self about how django handles sql:
    1. IDs as PKs are created automatically
    2. You have to run makemigration on the app name to create the the migration,
        and then run migrate to actually migrate the changes to the database
"""
    
class StudioBooking(models.Model):
    first_name = models.CharField(max_length=50, default='None')
    last_name = models.CharField(max_length=50, default='None')
    band_name = models.CharField(max_length=100, default='None')
    start_date = models.CharField(max_length=20, default='None')
    end_date = models.CharField(max_length=20, default='None')
    engineer = models.CharField(max_length=40)
    studio = models.CharField(max_length=20)
    cost_per_hour = models.FloatField()
    est_total_cost = models.FloatField()

    def __str__(self):
        summary = f"First Name: {self.first_name}\n\
                    Last Name: {self.last_name}\n\
                    Band Name: {self.band_name}\n\
                    Start Date: {self.start_date}\n\
                    End Date: {self.end_date}\n\
                    Engineer: {self.engineer}\n\
                    Studio: {self.studio}\n\
                    Cost/Hour: {self.cost_per_hour}\n\
                    Est Total Cost: {self.est_total_cost}"
        
        return summary
