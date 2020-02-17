# coding: utf-8
from django.urls import path,re_path

from . import views
app_name = 'activities'
urlpatterns = [
    re_path(r'^follow/$', views.follow, name='follow'),
    re_path(r'^unfollow/$', views.unfollow, name='unfollow'),
    re_path(r'^update_followers_count/$', views.update_followers_count, name='update_followers_count'),
    re_path(r'^(?P<username>[^/]+)/following/$', views.following, name='following'),
    re_path(r'^(?P<username>[^/]+)/followers/$', views.followers, name='followers')
]
