from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('logout/',views.logout_user,name="logout"),
    path('login',views.login_in,name='login'),
    path('signin',views.registration,name='signin'),
    path('card_team/<int:team_id>',views.card_team,name='card_team'),
    path('show_card_team',views.show_card_team,name='show_card_team'),
    path('delete/<int:id>', views.delete, name='delete'),
]