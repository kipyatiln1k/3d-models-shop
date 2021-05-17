from django.shortcuts import render
from django.views.generic import DetailView

from mdls.models import Mdl


class MdlDetailView(DetailView):
    model = Mdl
    template_name = "mdls/detail.html"
