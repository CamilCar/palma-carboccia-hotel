from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import BookingForm

# Create your views here.


def booking_page(request):
    booking_form = BookingForm()
    print(booking_form)

    return render(request, "booking/booking.html", {
        "booking_form": booking_form
})


def reservation_summary(request):
    return render(request, "booking/reservation_summary.html")


@login_required
def new_booking(request):
    render(request, 'booking/booking_successful.html')
