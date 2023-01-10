from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, DeleteView
from django.views import View
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Group
from .forms import GroupForm


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


class Search(List):
    def get_queryset(self, *args, **kwargs):
        filter = self.request.GET.get('filter')
        qs = super().get_queryset(*args, **kwargs)

        if not filter:
            return qs

        qs = qs.filter(Q(code__icontains=filter) | Q(name__icontains=filter) | Q(description__icontains=filter))
        return qs


class New(DispatchLoginRequiredMixin, View):
    template_name = 'group_new.html'

    def get(self, *args, **kwargs):
        form = GroupForm()
        context = {
            'form': form
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = GroupForm(self.request.POST)

        if not form.is_valid():
            messages.error(self.request, 'Alguns problemas foram encontrados em seu cadastro. '
                                         'Verifique os campos e tente novamente.')
            return render(self.request, self.template_name, {'form': form})

        group = Group(**form.cleaned_data)
        group.save()

        messages.success(self.request, 'Grupo salvo com sucesso.')
        return redirect('group:list')


class Detail(DispatchLoginRequiredMixin, DetailView):
    pass


class Delete(DispatchLoginRequiredMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('group:list')
