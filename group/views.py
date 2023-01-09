from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Group


class DispatchLoginRequiredMixin(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authentication:login')

        return super().dispatch(*args, **kwargs)


class List(DispatchLoginRequiredMixin, ListView):
    template_name = 'group_list.html'
    model = Group
    context_object_name = 'groups'
    paginate_by = 10
    ordering = ['-id']


class Search(DispatchLoginRequiredMixin, ListView):
    pass


class New(DispatchLoginRequiredMixin, View):
    pass


class Detail(DispatchLoginRequiredMixin, DetailView):
    pass


class Delete(DispatchLoginRequiredMixin, View):
    pass
