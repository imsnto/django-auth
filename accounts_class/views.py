from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.contrib.auth import login
from .forms import RegisterForm
from django.urls import reverse_lazy



class RegisterView(FormView):
    template_name = 'accounts_class/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('accounts_class:home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        form.save()
        login(self.request, user) 
        return super().form_valid(form)

class HomeView(TemplateView):
    template_name = 'accounts_class/home.html'
    