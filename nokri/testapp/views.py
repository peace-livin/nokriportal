from django.shortcuts import render
from testapp.models import Mumbai, Pune, Hyderabad
# Create your views here.

def home(request):
    return render(request, 'testapp/home.html')

def mumbai_view(request):
    job_list = Mumbai.objects.all()
    return render(request, 'testapp/mumbai.html', {'job_list': job_list})

def pune_view(request):
    job_list = Pune.objects.all()
    return render(request, 'testapp/pune.html', {'job_list': job_list})

def hyd_view(request):
    job_list = Hyderabad.objects.all()
    return render(request, 'testapp/hydrabad.html', {'job_list': job_list})

