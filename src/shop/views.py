from django.shortcuts import render
from django.views.generic import ListView
from mdls.forms import MdlTagSearchFrom
from django.urls.base import reverse_lazy


from mdls.models import Mdl
from shop.utils import filter_by_tags

class MdlListView(ListView):
    model = Mdl
    paginate_by = 20
    template_name = 'shop/home.html'
    form_class = MdlTagSearchFrom
    
    # def get(self, request, *args, **kwargs):
    #     mdls = self.get_queryset()
    #     if request.GET.get('tags'):
    #         tags = request.GET.get('tags')
    #         mdls = filter_by_tags(tags)
    #         return render(request, self.template_name, {'stuff': mdls, 'tags': tags }) 
    #     return render(request, self.template_name, {'stuff': mdls}) 
        
    def post(self, request, *args, **kwargs):
        tags = request.POST.get('tags')
        qs = self.get_queryset().get(tags_contains=tags)
        return render(request, self.template_name, {'qs': qs, 'tags': tags })
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        form = MdlTagSearchFrom()
        context['form'] = form
        
        context['action'] = reverse_lazy('cities:create')
        
        return context