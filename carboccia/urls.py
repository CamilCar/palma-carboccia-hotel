"""carboccia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import landing_page, history_page, rooms_page, food_page, price_page
from booking.views import booking_page
from reservation.views import reservation_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_page, name='home'),
    path('landing_page', landing_page, name='home'),
    path('the_hotel', history_page, name='the_hotel'),
    path('our_rooms', rooms_page, name='our_rooms'),
    path('food_drink', food_page, name='food_drink'),
    path('prices', price_page, name='prices'),
    path('booking', booking_page, name='book_a_room'),
    path('reservation', reservation_page, name='reservation'),
    path('accounts/', include('allauth.urls')),
    ]
