import email
from django.shortcuts import render
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
      email=request.POST['email']
      name=request.POST['name']
      message=request.POST['message']
      contact = Contact.objects.create(
         email=email,
         name=name,
         message=message
      )
      messages.success(request, 'تم الارسال بنجاح')

    
    return render(request,'contact.html')