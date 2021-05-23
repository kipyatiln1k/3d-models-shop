from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from mdls.models import Mdl



class MdlDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('accounts:login')
    model = Mdl
    template_name = "mdls/detail.html"
    

    