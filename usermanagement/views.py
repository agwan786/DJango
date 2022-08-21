import hashlib

from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from usermanagement.models import Customer


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)
        email = request.POST.get('email', False)
        if Customer.objects.filter(email=email).exists():
            messages.info(request, 'Customer with same email id is already exists')
            return redirect('/signup')
        else:
            if password1 != '' and password1 == password2:
                customers = Customer.objects.create(password=hashlib.md5(password1.encode()).hexdigest(), email=email,
                                                    first_name=first_name,
                                                    last_name=last_name)
                customers.save()
                messages.info(request, 'Successfully customer created....')
                return redirect('/users')
            else:
                messages.info(request, 'Some issue with your input....')
                return redirect('/signup')
    else:
        customers = Customer.objects.all()
        return render(request, 'signup.html', {'customers': customers})

def users(request):
    customers = Customer.objects.all()
    return render(request, 'users.html', {'customers': customers})
