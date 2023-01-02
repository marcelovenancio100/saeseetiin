from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views import View


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authentication:login')

        return super().dispatch(*args, **kwargs)


class List(DispatchLoginRequiredMixin, ListView):
    pass


class Search(DispatchLoginRequiredMixin, ListView):
    pass


class Detail(DispatchLoginRequiredMixin, DetailView):
    pass
