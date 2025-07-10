from django.shortcuts import render
from testapp.models import Mumbai, Pune, Hyderabad
# Create your views here.

def home(request):
    return render(request, 'testapp/home.html')

def mumbai(request):
    mumbai = Mumbai.objects.all()
    return render(request, 'testapp/mumbai.html', {'mumbai': mumbai})

def pune(request):
    pune = Pune.objects.all()
    return render(request, 'testapp/pune.html', {'pune': pune})

def hyd(request):
    hydrabad = Hyderabad.objects.all()
    return render(request, 'testapp/hydrabad.html', {'hydrabad': hydrabad})
