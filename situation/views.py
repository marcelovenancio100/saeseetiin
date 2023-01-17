from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Situation
from .forms import SituationForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'situation_list.html'
    model = Situation
    context_object_name = 'situations'
    paginate_by = 10
    ordering = ['-id']


class Search(List):
    def get_queryset(self, *args, **kwargs):
        filter = self.request.GET.get('filter')
        qs = super().get_queryset(*args, **kwargs)

        if not filter:
            return qs

        qs = qs.filter(Q(code__icontains=filter) | Q(name__icontains=filter) | Q(description__icontains=filter))
        return qs


class Create(LoginRequiredMixinCustom, SuccessMessageMixin, CreateView):
    template_name = 'situation_form.html'
    form_class = SituationForm
    success_url = reverse_lazy('situation:list')
    success_message = 'Situação criada com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'situation_form.html'
    model = Situation
    fields = ['code', 'name', 'description']
    success_url = reverse_lazy('situation:list')
    success_message = 'Situação atualizada com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = Situation
    success_url = reverse_lazy('situation:list')
    success_message = 'Situação excluída com sucesso.'
