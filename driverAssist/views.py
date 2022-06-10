from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'driverAssist/home.html')

def navigation(request):
    return render(request, 'driverAssist/navigation.html')