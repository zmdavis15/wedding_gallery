from django.shortcuts import render
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView,
                                  DeleteView, FormView, TemplateView)
from .forms import PhotoForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView


# Create your views here.
class TestedAssemblyCreateView(BSModalCreateView):
    template_name = 'photos/photos.html'
    form_class = PhotoForm
    success_message = 'Photo Uploaded successfully!'
    success_url = reverse_lazy('layout:index')
