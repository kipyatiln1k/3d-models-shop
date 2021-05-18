from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from mdls.forms import MdlTagSearchForm
from django.urls.base import reverse_lazy


from mdls.models import Mdl, Tag
from shop.utils import filter_by_tags


class MdlListView(ListView):
    model = Mdl
    paginate_by = 20
    template_name = 'shop/home.html'
    form_class = MdlTagSearchForm
    
    
    def post(self, request, *args, **kwargs):
        tags_ids = request.POST.getlist('tags')
        tags = Tag.objects.filter(id__in=tags_ids)
        # print(Tag.objects.values())
        # print(tags_ids)
        # print(tags)
        # print(filter_by_tags(tags))
        
        return render(request, self.template_name, {'page_obj': filter_by_tags(tags), 'form': self.form_class()})
        
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = MdlTagSearchForm()
        context['form'] = form
        
        return context
    
    

class MdlSearchListView(MdlListView):
    object_list = Mdl
    
    def __init__(self, *args, **kwargs):
        super(MdlListView, self).__init__(*args, **kwargs)
        if 'object_list' in kwargs.keys():
            self.object_list = kwargs['object_list']
    