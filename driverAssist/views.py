from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'driverAssist/home.html')

def signin(request):
    return render(request, 'driverAssist/signin.html')

def navigation(request):
    return render(request, 'driverAssist/navigation.html')

def students(request):
    return render(request, 'driverAssist/students.html')
