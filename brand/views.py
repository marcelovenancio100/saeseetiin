from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from .models import Brand
from .forms import BrandForm
from mixins.custom_mixins import LoginRequiredMixinCustom


class List(LoginRequiredMixinCustom, ListView):
    template_name = 'brand_list.html'
    model = Brand
    context_object_name = 'brands'
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
    template_name = 'brand_form.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand:list')
    success_message = 'Marca criada com sucesso.'


class Update(LoginRequiredMixinCustom, SuccessMessageMixin, UpdateView):
    template_name = 'brand_form.html'
    model = Brand
    fields = '__all__'
    success_url = reverse_lazy('brand:list')
    success_message = 'Marca atualizada com sucesso.'


class Delete(LoginRequiredMixinCustom, SuccessMessageMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('brand:list')
    success_message = 'Marca excluída com sucesso.'
