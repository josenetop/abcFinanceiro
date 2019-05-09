from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from app_accounts.views import Login


urlpatterns = [
    
    path('', Login.as_view(), name='login'),
    #path('', Logout.as_view(), name='logout'),
    #path('logout/', login_required(Logout.as_view()), name='logout_abc'),

    #path('', include('django.contrib.auth.urls')),

]