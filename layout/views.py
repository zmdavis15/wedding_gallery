from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from photos.models import Photo


class IndexView(ListView):
    template_name = "layout/index.html"
    model = Photo
    ordering = ['-date']
    paginate_by = 10  # if pagination is desired

    def get_queryset(self):
        order = self.request.GET.get('orderby')
        if order == 'Descending':
            sort_order = '-date'
        elif order == 'Ascending':
            sort_order = 'date'
        else: #default
            sort_order = '-date'
        new_context = Photo.objects.order_by(sort_order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        sort_order = self.request.GET.get('orderby')
        context['sort_order'] = sort_order
        return context
