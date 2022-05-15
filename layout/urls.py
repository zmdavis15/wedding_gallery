from django.urls import include, path
from . import views
from .views import IndexView

app_name = 'layout'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
