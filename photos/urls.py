from django.urls import include, path
from . import views
from .views import TestedAssemblyCreateView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'photos'

urlpatterns = [
    path('photos/create', TestedAssemblyCreateView.as_view(), name='photo_create'),
]
