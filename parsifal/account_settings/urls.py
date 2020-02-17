# coding: utf-8
from django.conf.urls import include, url
from . import views

app_name = 'account_settings'
urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^emails/$', views.emails, name='emails'),
    url(r'^picture/$', views.picture, name='picture'),
    url(r'^password/$', views.password, name='password'),

    url(r'^connections/$', views.connections, name='connections'),
    
    url(r'^mendeley_connection/$', views.mendeley_connection, name='mendeley_connection'),
    url(r'^connect_mendeley/$', views.connect_mendeley, name='connect_mendeley'),
    url(r'^disconnect_mendeley/$', views.disconnect_mendeley, name='disconnect_mendeley'),

    url(r'^dropbox_connection/$', views.dropbox_connection, name='dropbox_connection'),
    url(r'^connect_dropbox/$', views.connect_dropbox, name='connect_dropbox'),
    url(r'^disconnect_dropbox/$', views.disconnect_dropbox, name='disconnect_dropbox'),

    url(r'^upload_picture/$', views.upload_picture, name='upload_picture'),
    url(r'^save_uploaded_picture/$', views.save_uploaded_picture, name='save_uploaded_picture'),
]
