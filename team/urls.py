from team import views
from django.urls import path

app_name="team"
urlpatterns = [
    path('team',views.team,name='team'),
    path('<int:id>',views.singleteam,name='singleteam'),
]
