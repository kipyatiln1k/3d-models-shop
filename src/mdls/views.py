from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from mdls.forms import MdlForm

from mdls.models import Mdl



class MdlDetailView(LoginRequiredMixin, DetailView):
    # login_url = reverse_lazy('accounts:login')
    model = Mdl
    template_name = "mdls/detail.html"
    
    
class MdlCreateView(LoginRequiredMixin, CreateView):
    model = Mdl
    form_class = MdlForm
    template_name = "mdls/create.html"
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('accounts:login')

    

    