from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User

from .forms import UserForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'user_list.html'
    model = User
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['-id']


class Search(List):
    def get_queryset(self, *args, **kwargs):
        filter = self.request.GET.get('filter')
        qs = super().get_queryset(*args, **kwargs)

        if not filter:
            return qs

        qs = qs.filter(Q(username__icontains=filter) | Q(first_name__icontains=filter) | Q(last_name__icontains=filter))
        return qs


class Create(LoginRequiredMixinCustom, SuccessMessageMixin, CreateView):
    template_name = 'user_form.html'
    form_class = UserForm
    success_url = reverse_lazy('user:list')
    success_message = 'Usuário criado com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'user_form.html'
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('user:list')
    success_message = 'Usuário atualizado com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = User
    success_url = reverse_lazy('user:list')
    success_message = 'Usuário excluído com sucesso.'
