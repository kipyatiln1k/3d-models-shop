from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from mdls.forms import MdlTagSearchForm
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required


from mdls.models import Mdl, Tag
from shop.utils import filter_by_tags


class MdlListView(ListView):
    model = Mdl
    paginate_by = 20
    template_name = 'shop/home.html'
    form_class = MdlTagSearchForm
    
    def get_queryset(self):
        tags_ids = self.request.GET.getlist('tags', Tag.objects.all().values_list('id', flat=True))
        order = self.request.GET.get('order', 'date')
        new_context = filter_by_tags(Tag.objects.filter(
            id__in=tags_ids,
        )).order_by(order)
        return new_context
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = MdlTagSearchForm()
        context['form'] = form
        
        context['tags'] = self.request.GET.get('tags', Tag.objects.all().values_list('id', flat=True))
        context['order'] = self.request.GET.get('order', 'date')
        
        return context    
    
