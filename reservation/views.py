from django.shortcuts import render

# Create your views here.


def reservation_page(request):

    return render(request, "reservation/reservation.html")
