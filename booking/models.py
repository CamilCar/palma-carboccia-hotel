from django.contrib.auth.models import User
from django.db import models


class Booking(models.Model):
    """
    Set up the bookings table in db
    with all the required fields, such
    as dates, adults and kids. Checks
    if its the right data type.
    """
    start_date = models.DateField()
    end_date = models.DateField()
    amount_adults = models.IntegerField()
    amount_kids = models.IntegerField(blank=True, null=True)
    total_price = models.FloatField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='bookings', on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name
