from django.views import generic
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserForm, LoginForm



class RegisterView(generic.CreateView):
    form_class = CustomUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login")



class AuthLoginView(generic.FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class AuthLogoutView(generic.RedirectView):
    url = reverse_lazy("login")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context