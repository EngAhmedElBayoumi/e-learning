from django.shortcuts import render
from team.models import Reservation

# Create your views here.
def home(request):
    return render(request,'index.html')

def information(request):
    reservation=Reservation.objects.all()
    context={
        'team':reservation
    }
    return render(request,'information.html',context)


