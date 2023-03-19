from django.contrib.auth.models import User
from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    amount_adults = models.IntegerField()
    amount_kids = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    total_price = models.FloatField()
    created_by = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
