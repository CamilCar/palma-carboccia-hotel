from django.shortcuts import render

# Create your views here.


def landing_page(request):

    return render(request, "nav_section/index.html")

def history_page(request):

    return render(request, "nav_section/the_hotel.html")

def rooms_page(request):

    return render(request, "nav_section/our_rooms.html")

def food_page(request):

    return render(request, "nav_section/food_drink.html")

def price_page(request):

    return render(request, "nav_section/prices.html")

