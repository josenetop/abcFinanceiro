from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import (HttpResponse,
                        HttpResponseRedirect,
                        HttpResponseForbidden,
                        HttpResponseBadRequest,
                        JsonResponse)
from app_accounts.models import *

from django.views.generic.base import TemplateView

# Create your views here.
class login(View):
    context = {}
    def get(self, request):
        template_name = 'login.html'
        print('entrou no get')
        return render(resquest, template_name)
    
    def post(self, request):
        context = {}
        username = request.POST['username']
        senha = request.POST['senha']
        user = authenticate(user=username, password=senha)
        if user is not None:
            print('Está logando')
            login(request, user)
            if not request.user.is_anonymous:
                usuario = DefaultUser.objects.get(usuario=request.user.id_usuario)
                context['mensagem'] = 'Passou!'
                return render(request, context)
        else:
            context['mensagem'] = 'Email ou senha incorretos!'
            return render(request, 'login.html', context)