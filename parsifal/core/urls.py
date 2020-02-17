from django.urls import path,re_path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', TemplateView.as_view(template_name='core/about.html'), name='about')
]
