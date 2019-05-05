from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.urls import views

from app_accounts.views import *

urlpatterns = [
    path('', views.LoginView.as_view(), name='login_abc'),
    #path('logout/', login_required(Logout.as_View()), name='logout_abc'),
    #path('home/', login_required(Home.as_View()), name='home_abc'),

    #path('', include('django.contrib.auth.urls')),
]
