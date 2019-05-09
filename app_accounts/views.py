from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.contrib.auth.decorators import login_required
from django.http import __all__

from app_accounts.models import *
# Create your views here.

class Login(View):
    context = {}
    def get(self, request):
        template_name = 'registration/login.html'
        return render(request, template_name, self.context)

    def post(self, request):
        usuario = request.POST['email']
        senha = request.POST['senha']
        user = authenticate(username=usuario, password=senha)
        print(user)
        if user is not None:
            login(request, user)
            if not request.user.is_anonymous:
                username = auth_user.object.get(username=request.user.id)
                return render(request, 'home.html')
        else:
            context['mensagem'] = 'Usuário ou senha incorretos!'
            return render(request, 'registration/login.html', context)

#class Logout(View):
#    def get(self, request):
#        if request.user.is_authenticated:
#            logout(request)
#            return render(request, 'registration/login.html')