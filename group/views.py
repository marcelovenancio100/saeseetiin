from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.db.models import Q

from .models import Group
from .forms import FormGroup


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

        self.request.session['filter'] = filter
        self.request.session.save()

        qs = qs.filter(Q(code__icontains=filter) | Q(name__icontains=filter) | Q(description__icontains=filter))
        return qs


class New(DispatchLoginRequiredMixin, View):
    template_name = 'group_new.html'

    def get(self, *args, **kwargs):
        form = FormGroup()
        context = {
            'form': form
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = FormGroup(self.request)

        if form.is_valid():
            print(form)


class Detail(DispatchLoginRequiredMixin, DetailView):
    pass


class Delete(DispatchLoginRequiredMixin, View):
    pass
