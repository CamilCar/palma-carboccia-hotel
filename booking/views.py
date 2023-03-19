from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import BookingForm, ConfirmBookingForm

# Create your views here.


def booking_page(request):
    if request.method == "POST":
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            confirm_booking_dict = {
                    'start_date': request.POST.get('start_date'),
                    'end_date': request.POST.get('end_date'),
                    'amount_adults': request.POST.get('amount_adults'),
                    'amount_kids': request.POST.get('amount_kids'),
                    'total_price': 100
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
    render(request, 'booking/booking_successful.html')
