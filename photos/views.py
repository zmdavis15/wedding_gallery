from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, FormView, TemplateView)
from .forms import PhotoForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# Create your views here.
class TestedAssemblyCreateView(CreateView):
    template_name = 'photos/photos.html'
    form_class = PhotoForm
    success_message = 'Photo Uploaded successfully!'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        self.success_url = reverse_lazy('layout:index')
        return super(TestedAssemblyCreateView, self).form_valid(form)
