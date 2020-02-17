# coding: utf-8

from django.urls import path,re_path,include
from . import views

app_name = 'reviews.reporting'
urlpatterns = [
    re_path(r'^download_docx/$', views.download_docx, name='download_docx'),
]
