from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from django.http import HttpResponseNotFound

from .forms import BookingForm, ConfirmBookingForm, EditBookingForm
from .models import Booking


# This is where the first step of booking is handled
@login_required
def booking_page(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)

        # Check if form is valid , render and sends data to the reservation_summary page
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
        # If user selects faulty days
        else:
            booking_form = BookingForm()
            return render(request, "booking/booking.html", {
                "booking_form": booking_form,
                "end_date_error": 'The end date has to be later than the start date'
            })
    # Handles GET request
    else:
        booking_form = BookingForm()
        return render(request, "booking/booking.html", {
            "booking_form": booking_form
        })


# Saves the new booking to db
@login_required
def new_booking(request):

    form = ConfirmBookingForm(request.POST)

    if form.is_valid():
        new_booking = form.save(commit=False)
        new_booking.created_by = request.user

        amount_of_adults = new_booking.amount_adults
        amount_of_children = new_booking.amount_kids
        amount_of_nights = (new_booking.end_date - new_booking.start_date).days

        new_booking.total_price = calculate_price(amount_of_adults, amount_of_children, amount_of_nights)
        new_booking.save()

        return redirect('booking_successful')


# Renders booking_successful
@login_required
def booking_successful(request):
    return render(request, 'booking/booking_successful.html')


# Shows user reservations
def my_reservations(request):
    reservations = Booking.objects.filter(created_by=request.user)

    return render(request, 'booking/my_reservations.html', {
        'reservations': reservations
    })


# Let user delete reservation
@login_required
def delete_reservation(request, pk):
    reservation = get_object_or_404(Booking, pk=pk, created_by=request.user)
    reservation.delete()

    return redirect("my_reservations")


# Let user edit reservation
@login_required
def edit_reservation(request, pk):
    reservation = get_object_or_404(Booking, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditBookingForm(request.POST, instance=reservation)
        # Checks if new user input is valid
        if form.is_valid():
            new_booking = form.save(commit=False)
            amount_of_adults = new_booking.amount_adults
            amount_of_children = new_booking.amount_kids
            amount_of_nights = (new_booking.end_date - new_booking.start_date).days
            # Updates the price
            new_booking.total_price = calculate_price(amount_of_adults, amount_of_children, amount_of_nights)
            new_booking.save()
            return redirect('my_reservations')
    else:
        booking_form = EditBookingForm(instance=reservation)

        return render(request, 'booking/edit_reservation.html', {
            'reservation': booking_form
        })


# Calculates the price
def calculate_price(amount_of_adults: int, amount_of_children: int, amount_of_nights: int):
    initial_price = 50
    price_per_adult = 50
    price_per_child = 25

    return (initial_price + (amount_of_adults * price_per_adult) + (amount_of_children * price_per_child)) * amount_of_nights
