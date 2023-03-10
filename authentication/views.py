from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from utils.menu_data import MENU_ITEMS


class Login(View):
    def get(self, *args, **kwargs):
        template_name = 'login.html'
        context = {}

        return render(self.request, template_name, context)

    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(self.request, 'Usuário ou senha inválidos!')
            return redirect('authentication:login')

        usuario = authenticate(self.request, username=username, password=password)

        if not usuario:
            messages.error(self.request, 'Usuário ou senha inválidos!')
            return redirect('authentication:login')

        login(self.request, user=usuario)

        self.request.session['menu_items'] = MENU_ITEMS
        self.request.session.save()

        return redirect('home:home')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)

        return redirect('authentication:login')
