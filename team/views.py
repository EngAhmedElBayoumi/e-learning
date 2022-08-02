from django.shortcuts import render
from .models import teams,Reservation
from accounts.models import Profile
from django.contrib import messages

# Create your views here.
def team(request):
    team=teams.objects.all()

    context={'team':team}
    return render(request,'team.html',context)


def singleteam(request,id):
    team=teams.objects.get(id=id)
    context={'team':team}
    return render(request,'single.html',context)

