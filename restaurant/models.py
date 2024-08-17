from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    first_name = models.CharField(max_length=200)    
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000, blank=True)
    booking_date = models.DateTimeField(db_index=True)

    def __str__(self):
        return f"{self.first_name} - {self.booking_date}"


class Menu(models.Model):
    name = models.CharField(max_length=200)    
    price = models.IntegerField(null=False)
    description = models.CharField(max_length=1000, blank=True) 

    def __str__(self):
        return self.name
        