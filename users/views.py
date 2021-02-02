from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm

class SignupPageView(CreateView):

    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')