from django.shortcuts import redirect
from django.views import View


class LoginRequiredMixinCustom(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect('authentication:login')

        return super().dispatch(*args, **kwargs)
