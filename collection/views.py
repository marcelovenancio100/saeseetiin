from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Collection
from .forms import CollectionForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'collection_list.html'
    model = Collection
    context_object_name = 'collections'
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
    template_name = 'collection_form.html'
    form_class = CollectionForm
    success_url = reverse_lazy('collection:list')
    success_message = 'Coleção criada com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'collection_form.html'
    model = Collection
    fields = ['code', 'name', 'description', 'owner', 'responsible', 'comments']
    success_url = reverse_lazy('collection:list')
    success_message = 'Coleção atualizada com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = Collection
    success_url = reverse_lazy('collection:list')
    success_message = 'Coleção excluída com sucesso.'
