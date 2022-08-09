from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Zapato, Cliente, Venta
from django.urls import reverse_lazy


# Create your views here.
class ZapatoListView(ListView):
    model = Zapato
    template_name = 'listarzapatos.html'
    context_object_name = 'zapatos'

class ZapatoDetailView(DetailView):
    model = Zapato
    template_name = 'detallarzapato.html'
    context_object_name = 'zapato'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.filter(zapato=self.object)
        return context

class ZapatoCreateView(CreateView):
    model = Zapato
    template_name = 'crearzapato.html'
    fields = '__all__'
    success_url = '/'

class ZapatoUpdateView(UpdateView):
    model = Zapato
    template_name = 'actualizarzapato.html'
    context_object_name = 'zapato'
    fields = '__all__'
    success_url = '/'

class ZapatoDeleteView(DeleteView):
    model = Zapato
    template_name = 'borrarzapato.html'
    context_object_name = 'zapato'
    success_url = '/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_not_delete'] = reverse_lazy('listarzapatos') 
        return context
    