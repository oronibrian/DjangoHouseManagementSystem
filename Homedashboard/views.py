import datetime

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required
from Homedashboard.models import Room, Tenant
from .forms import UserLoginForm


def login_view(request):
      home = request.POST.get('home','/index/')
      print (request.user.is_authenticated())
      title='Login'
      form =UserLoginForm(request.POST or None)
      if form.is_valid():
          username = form.cleaned_data.get("username")
          password = form.cleaned_data.get('password')
          user = authenticate(username=username, password=password)
          login(request,user)
          print (request.user.is_authenticated())
          return HttpResponseRedirect(home)

      return render(request,'login.html',{'form':form,'title':title})

def logout_view(request):
    home = request.POST.get('home', '/index/')
    logout(request)
    title = 'Login'
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponseRedirect(home)
    return render(request, 'login.html', {'form': form, 'title': title})


@login_required
def index(request):
    template = loader.get_template('homedashboard.html')
    context = {
        'freerooms': Room.objects.all().filter(status='Free').count(),
        'takenrooms': Room.objects.all().filter(status='Taken').count(),
        'today':datetime.datetime.now().date()

    }

    return  HttpResponse(template.render(context, request))


def createuser(request):
    return render(request, "CreateUser.html")


def newtenant(request):
    # This loads the room numbers to the dropdown list
    template = loader.get_template('newtenant.html')
    context = {
        'rooms': Room.objects.all()
    }

    # Submiting information to the database

    if request.method == 'POST':
        firstname = request.POST.get('firstname', False)
        secondname = request.POST.get('secondname', False)
        occupation = request.POST.get('occupation', False)
        email = request.POST.get('email', False)
        description = request.POST.get('description', False)
        roomnumber = request.POST.get('room_no', False)
        nooftenant = request.POST.get('no_of_tenants', False)

        Tenant.objects.create(
            firstname=firstname,
            secondname=secondname,
            occupation=occupation,
            email=email,
            description=description,
            roomnumber=roomnumber,
            nooftenant=nooftenant

        )

    return HttpResponse(template.render(context, request))


def tenant(request):
    template = loader.get_template('tenant.html')
    context = {
        'tenants': Tenant.objects.all()
    }

    return HttpResponse(template.render(context, request))


# Adding rooms
def roomregistration(request):
    if request.method == 'POST':
        roomno = request.POST['roomno']
        floor = request.POST['floor']
        status = request.POST['status']

        Room.objects.create(
            roomno=roomno,
            floor=floor,
            status=status
        )
    return render(request, "roomregistration.html")


# Retrieving all rooms
def rooms(request):
    template = loader.get_template('rooms.html')
    context = {
        'rooms': Room.objects.all()
    }
    return HttpResponse(template.render(context, request))




