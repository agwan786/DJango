from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Content


# Create your views here.
def index(request):
    cont1 = Content()
    cont1.id = 1
    cont1.name = 'Dainik Bhaskar'
    cont1.overview = 'Dainik Bhaskar is an Indian Hindi-language daily newspaper owned by the Dainik Bhaskar Group. ' \
                     'According to Audit Bureau of Circulations, it is ranked 4th in the world by circulation and 1st' \
                     ' in India '
    cont1.image = 'logo.png'

    cont2 = Content()
    cont2.id = 2
    cont2.name = 'Reliance Jio'
    cont2.overview = 'Reliance Jio Infocomm Limited, d/b/a Jio, is an Indian telecommunications company and a ' \
                     'subsidiary of Jio Platforms, headquartered in Mumbai, Maharashtra, India '
    cont2.image = 'logo.png'

    cont3 = Content()
    cont3.id = 3
    cont3.name = 'Tech Mahindra'
    cont3.overview = 'Tech Mahindra is an Indian multinational technology company, providing information technology ' \
                     'and business process outsourcing services. A subsidiary of the Mahindra Group, the company is ' \
                     'headquartered in Pune and has its registered office in Mumbai. '
    cont3.image = 'logo.png'

    cont = [cont1, cont2, cont3]
    return render(request, 'build.html', {'data': cont})


def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', False)
        last_name = request.POST.get('last_name', False)
        username = request.POST.get('username', False)
        password1 = request.POST.get('password1', False)
        password2 = request.POST.get('password2', False)
        email = request.POST.get('email', False)

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
        user.save()
        print('user created')
        return redirect('/index')
    else:
        return render(request, 'signup.html')


def adduser(request):
    username = str(request.POST.get('username', False))
    email = str(request.POST.get('email', False))
    pwd = str(request.POST.get('password', False))
    cpd = str(request.POST.get('password1', False))
    if pwd == cpd:
        return HttpResponse(username)
    else:
        return HttpResponse('Password not meet')
