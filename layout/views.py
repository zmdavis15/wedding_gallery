from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from photos.models import Photo


class IndexView(ListView):
    template_name = "layout/index.html"
    model = Photo
    ordering = ['-date']
    paginate_by = 10  # if pagination is desired

    # def get(self, request, *args, **kwargs):
    #     print(request)
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def get_context_data(self, **kwargs):
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     if self.request.GET.get('filter'):
    #             filter = self.request.GET.get('filter')
    #             print(self.request)
    #             # filter_set = filter_set.filter(type=type)
    #
    #     return context
