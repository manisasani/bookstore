from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import CustomuserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomuserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')