from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse("Altaf Husain")


def as_view(request):
    return render(request, 'home.html', {'name': 'Altaf Agwan'})


def add(request):
    var1 = float(request.POST['num1'])
    var2 = float(request.POST['num2'])
    sumVal = var1 + var2
    return render(request, 'home.html', {'result': sumVal, 'name': 'Altaf Agwan'})
