from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Model
from .forms import ModelForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'model_list.html'
    model = Model
    context_object_name = 'models'
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
    template_name = 'model_form.html'
    form_class = ModelForm
    success_url = reverse_lazy('model:list')
    success_message = 'Modelo criado com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'model_form.html'
    model = Model
    fields = ['code', 'name', 'description', 'specifications', 'logo']
    success_url = reverse_lazy('model:list')
    success_message = 'Modelo atualizado com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = Model
    success_url = reverse_lazy('model:list')
    success_message = 'Modelo excluído com sucesso.'
