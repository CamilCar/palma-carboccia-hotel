from django.shortcuts import render

# Create your views here.


def landing_page(request):

    return render(request, "nav_section/index.html")

def history_page(request):

    return render(request, "nav_section/the_hotel.html")