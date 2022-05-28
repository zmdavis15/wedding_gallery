from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from photos.models import Photo


class IndexView(ListView):
    template_name = "layout/index.html"
    model = Photo
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
