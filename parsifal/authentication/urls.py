from django.urls import path,re_path

from . import views

app_name='authentication'
urlpatterns = [
    re_path(r'^signup/$', views.signup, name='signup'),
    re_path(r'^signin/$', views.signin, name='signin'),
    re_path(r'^signout/$', views.signout, name='signout'),
    re_path(r'^reset/$', views.reset, name='reset'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.reset_confirm, name='password_reset_confirm'),
    re_path(r'^success/$', views.success, name='success'),
]
