# coding: utf-8

from django.conf.urls import include, url
from . import views

app_name='library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list_actions/$', views.list_actions, name='list_actions'),
    url(r'^new_folder/$', views.new_folder, name='new_folder'),
    url(r'^edit_folder/$', views.edit_folder, name='edit_folder'),
    url(r'^folders/(?P<slug>[-\w]+)/$', views.folder, name='folder'),
    url(r'^new_shared_folder/$', views.new_shared_folder, name='new_shared_folder'),
    url(r'^shared/(?P<slug>[-\w]+)/$', views.shared_folder, name='shared_folder'),
    url(r'^new_document/$', views.new_document, name='new_document'),
    url(r'^documents/(?P<document_id>\d+)/$', views.document, name='document'),
    url(r'^move/$', views.move, name='move'),
    url(r'^copy/$', views.copy, name='copy'),
    url(r'^remove_from_folder/$', views.remove_from_folder, name='remove_from_folder'),
    url(r'^delete_documents/$', views.delete_documents, name='delete_documents'),
    url(r'^import_bibtex/$', views.import_bibtex, name='import_bibtex'),
]
