from django.shortcuts import render
from .models import Staff


# Create your views here.

def home(request):
    return render(request, 'home.html')


def staff(request):
    return render(request, 'staff.html')
