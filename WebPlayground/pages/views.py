from django.http.response import HttpResponse as HttpResponse
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView #Generic Edit
from django.urls import reverse_lazy
from .forms import PageForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required #login_required (para saver si un usuario esta registrado) #permision_required para saber si un usuario esta identificado y a la vez si tiene algun otro permiso

    
class PageListView(ListView):
    model = Page

class PageDetailView(DetailView):
    model = Page

@method_decorator(staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

@method_decorator(staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    object: Page
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.pk]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')  
class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')






