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


class Search(List):
    pass


class New(DispatchLoginRequiredMixin, View):
    pass


class Detail(DispatchLoginRequiredMixin, DetailView):
    pass


class Delete(DispatchLoginRequiredMixin, View):
    pass
