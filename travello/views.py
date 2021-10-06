from django.shortcuts import render

# Create your views here.
from .models import Destination


def index(request):
    dest1 = Destination()

    dest1.name = 'Mumbai'
    dest1.desc = "The city that never sleeps"
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = "First Biryani, then Sherwani"
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Banglore'
    dest3.desc = "Bautiful City"
    dest3.img = 'destination_3.jpg'
    dest3.price = 800
    dest3.offer = True

    dests = [dest1, dest2, dest3]
    dests = Destination.objects.all()
    return render(request, 'index.html', {'dests': dests})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
