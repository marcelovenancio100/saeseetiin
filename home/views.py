from django.shortcuts import render, redirect
from django.views import View

from utils.menu_data import MENU_ITEMS


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authentication:login')

        return super().dispatch(*args, **kwargs)


class Home(DispatchLoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        template_name = 'home.html'
        return render(self.request, template_name)
