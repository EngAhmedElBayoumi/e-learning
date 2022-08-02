from optparse import Option
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

choose=[
    ('الابتدائية','الابتدائية'),
    ('الاعدادية','الاعدادية'),
    ('الثانوية','الثانوية'),
]
class teams(models.Model):
    name = models.CharField(max_length=50,verbose_name = " اسم المدرس")
    Specialization= models.CharField(choices=choose,max_length=200,verbose_name = "المرحلة الدراسية")
    Subject= models.CharField(max_length=200,verbose_name = "المادة الدراسية")
    Abstract = models.TextField(verbose_name = " السيرة الذاتية")
    image=models.ImageField(upload_to=('static/teams/img'),blank=True,verbose_name = " الصورة الشخصية")
    video = models.FileField(upload_to='static/teams/video',blank=True,verbose_name = " فيديوا تعريفي")

    def __str__(self):
       return self.name


class Reservation(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    child_name=models.CharField(max_length=25,verbose_name = " اسم الطالب")
    parent_name=models.CharField(max_length=25,verbose_name = " اسم ولي الامر")
    address=models.CharField(max_length=25,verbose_name = "محل الاقامة")
    age=models.IntegerField(verbose_name = "محل الاقامة")
    barthdate=models.DateField(verbose_name = " تاريخ الميلاد")
    email=models.CharField(max_length=250,verbose_name = "البريد الالكتروني")
    phone=models.CharField(max_length=250,verbose_name = " رقم التلفون")
    comment=models.TextField(verbose_name ="ملاحظات ولي الامر")
    card_team=models.ManyToManyField(teams,verbose_name ="المدرسين")
   
    def __str__(self):
        return self.child_name

