from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from datetime import datetime

from .forms import BookingForm, ConfirmBookingForm
from .models import Booking


@login_required
def booking_page(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            amount_of_adults = int(request.POST.get('amount_adults') or "0")
            amount_of_children = int(request.POST.get('amount_kids') or "0")
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            
            amount_of_nights = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days

            confirm_booking_dict = {
                    'start_date': start_date,
                    'end_date': end_date,
                    'amount_adults': amount_of_adults,
                    'amount_kids': amount_of_children,
                    'total_price': calculate_price(amount_of_adults, amount_of_children, amount_of_nights)
            }

            confirm_booking_form = ConfirmBookingForm(confirm_booking_dict)

            return render(request, 'booking/reservation_summary.html', {
                "booking_form": confirm_booking_form
            })
    else:
        booking_form = BookingForm()
        return render(request, "booking/booking.html", {
            "booking_form": booking_form
        })


@login_required
def new_booking(request):
    # post the form to the database
    booking = Booking(request.POST)
    print(booking)

    # booking = form.save(commit=False)
    booking.created_by = request.user
    booking.save()

    return render(request, 'booking/booking_successful.html')


def calculate_price(amount_of_adults: int, amount_of_children: int, amount_of_nights: int):
    initial_price = 50
    price_per_adult = 50
    price_per_child = 25

    return (initial_price + (amount_of_adults * price_per_adult) + (amount_of_children * price_per_child)) * amount_of_nights


def my_reservations(request):
    return render(request, 'booking/my_reservations.html')
