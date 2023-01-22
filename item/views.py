from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Item
from .forms import ItemForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'item_list.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 10
    ordering = ['-id']


class Search(List):
    def get_queryset(self, *args, **kwargs):
        filter = self.request.GET.get('filter')
        qs = super().get_queryset(*args, **kwargs)

        if not filter:
            return qs

        qs = qs.filter(
            Q(code__icontains=filter) |
            Q(name__icontains=filter) |
            Q(description__icontains=filter) |
            Q(brand__icontains=filter) |
            Q(model__icontains=filter))
        return qs


class Create(LoginRequiredMixinCustom, SuccessMessageMixin, CreateView):
    template_name = 'item_form.html'
    form_class = ItemForm
    success_url = reverse_lazy('item:list')
    success_message = 'Item criado com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'item_form.html'
    model = Item
    fields = '__all__'
    success_url = reverse_lazy('item:list')
    success_message = 'Item atualizado com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item:list')
    success_message = 'Item excluído com sucesso.'


class Show(LoginRequiredMixinCustom, ListView):
    template_name = 'item_show.html'
    model = Item
    context_object_name = 'items'
    paginate_by = 3
    ordering = ['-id']


class ShowSearch(Show):
    def get_queryset(self, *args, **kwargs):
        filter = self.request.GET.get('filter')
        qs = super().get_queryset(*args, **kwargs)

        if not filter:
            return qs

        qs = qs.filter(
            Q(code__icontains=filter) |
            Q(name__icontains=filter) |
            Q(description__icontains=filter) |
            Q(brand__icontains=filter) |
            Q(model__icontains=filter))
        return qs


class Detail(LoginRequiredMixinCustom, DetailView):
    template_name = 'item_detail.html'
    model = Item
    context_object_name = 'item'

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        qs = Item.objects.select_related('collection', 'group', 'situation')
        return qs
