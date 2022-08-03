
from shutil import ReadError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.urls import is_valid_path
from .forms import LoginForm
from django.contrib import messages
from team.models import teams ,Reservation
from .models import Profile


# Create your views here.
def login_in(request):
    if request.method =='POST':
        form=LoginForm()
        username = request.POST['username']
        password = request.POST['password']
        user= authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('home:home')
        else:
           messages.warning(request,'هناك خطافى اسم المستخدم او كلمه المرور')
    else:
        form=LoginForm()
    return render(request, 'login.html',{
        'form': form,
    })

def logout_user(request):
    logout(request)
    return redirect('account:login')

def registration(request):
   
    if request.method =="POST":
      username = request.POST['username']
      password1 = request.POST['password1']
      password2 = request.POST['password2']
      email = request.POST['email']
    
      if password1== password2:
        myuser= User.objects.create_user(username,email,password1)
        myuser.save()
        return redirect('account:login')
           
      else:
           messages.error(request,'كلمه المرور غير متطابقه  ')
           return redirect('account:signin')
    else:  
     return render(request, 'sign-up.html')


def card_team(request,team_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        team_card=teams.objects.get(pk=team_id)
        if Profile.objects.filter(user=request.user,card_team=team_card).exists():
            messages.success(request,'تم الاضافة مسبقا للاستمارة')
        else:
            userteam=Profile.objects.get(user=request.user)
            userteam.card_team.add(team_card)
            messages.success(request,'تمت الاضافة بنجاح لاستمارة الحجز')
        
       
    else:
        messages.error(request,' يجب تسجيل الدخول اولا   ')

    return redirect('/team/' + str(team_id))

def show_card_team(request):
    context=None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userinfo=Profile.objects.get(user=request.user)
        card=userinfo.card_team.all()
        context={
            'team':card
        }
    if request.method == "POST":
        user=request.user
        child_name=request.POST['child_name']
        parent_name=request.POST['parent_name']
        address=request.POST['address']
        age=request.POST['age']
        barthdate=request.POST['barthdate']
        email=request.POST['email']
        phone=request.POST['phone']
        comment=request.POST['comment']
        card_team=card
        if request.user.is_authenticated and not request.user.is_anonymous:
            
            if Reservation.objects.filter(user=request.user).exists():

                reservation=Reservation.objects.get(user=request.user)
                card1=reservation.card_team.all()
                if child_name == reservation.child_name:
                    reservation.user=user
                    reservation.child_name=child_name
                    reservation.parent_name=parent_name
                    reservation.address=address
                    reservation.age=age
                    reservation.barthdate=barthdate
                    reservation.email=email
                    reservation.phone=phone
                    reservation.comment=comment
                    reservation.save()
                    reservation.card_team.remove(*card1)
                    reservation.card_team.add(*card)
                    messages.success(request,' تم تحديث الحجز بنجاح ')
                else:
                    messages.success(request,' لا يمكن الحجز لاكتر من طفل علي نفس الحساب يرجي انشاء حساب اخر والحجز')
            else:
                reservation=Reservation.objects.create(
                    user=user,
                    child_name=child_name,
                    parent_name=parent_name,
                    address=address,
                    age=age,
                    barthdate=barthdate,
                    email=email,
                    phone=phone,
                    comment=comment, 
                )
                userteam=Reservation.objects.get(user=request.user)
                userteam.card_team.add(*card)


                messages.success(request, 'تم الحجز بنجاح')
            
        else:
            messages.success(request,'يجب تسجيل الدخول اولا    ')

    return render(request,'class.html',context)

def delete(request, id):
  team_card=teams.objects.get(pk=id)
  userteam=Profile.objects.get(user=request.user)
  userteam.card_team.remove(team_card)
  messages.success(request,'  تم الحذف بنجاح من الاستمارة')
  return redirect('account:show_card_team')
  
 

    


