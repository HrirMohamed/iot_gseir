from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import DHT11
def hello_gsi4(request):
    return HttpResponse("Hello I am Professor")
def dashboard(request):
    mesure = DHT11.objects.order_by('-date').first()
    return render(request, 'dashboard.html', {'mesure': mesure})
