
from  django.urls import path,include
from . import views

app_name = 'music'
#urls for our main app

urlpatterns = [
path('',views.home_detail,name='home_detail'),
path('SignUp/',views.SignUp,name='SignUp'),
path('logout/',views.logout_user,name='logout_user'),
path('login/',views.login_user,name='login_user'),
path('(<album_id>[0-9]+)/', views.detail, name='detail'),
path('after_login_home/',views.after_login_home,name='after_login_home'),
path('(<song_id>[0-9]+)/', views.add, name='add'),
]