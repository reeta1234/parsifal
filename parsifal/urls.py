# coding: utf-8

from django.urls import include,path,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib import admin
from parsifal.reviews import views
from parsifal.reviews.settings import views as settingsView
from parsifal.activities import views as activitiesView
from parsifal.reviews.planning import views as planningView
from parsifal.reviews.conducting import views as conductingView
from parsifal.reviews.reporting import views as reportingView


admin.autodiscover()

urlpatterns = [
    path('', include('parsifal.core.urls')),
    path('settings/', include('parsifal.account_settings.urls',namespace='settings')),
    path('activities/', include('parsifal.activities.urls',namespace='activities')),
    path('authentication/', include('parsifal.authentication.urls',namespace='authentication')),
    path('blog/', include('parsifal.blog.urls', namespace='blog')),
    path('help/', include('parsifal.help.urls', namespace='help')),
    path('library/', include('parsifal.library.urls',namespace='library')),
    path('reviews/', include('parsifal.reviews.urls',namespace='reviews1')),
    path('admin/', admin.site.urls),
    re_path(r'^(?P<username>[^/]+)/$', views.reviews, name='reviews'),

    re_path(r'^sitemap.xml$', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    re_path(r'^robots.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    re_path(r'^(?P<username>[^/]+)/following/$', activitiesView.following, name='following'),
    re_path(r'^(?P<username>[^/]+)/followers/$', activitiesView.followers, name='followers'),

    # Review URLs
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/$', views.review, name='review'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/settings/$', settingsView.settings, name='settings'),
    
    # Planning Phase
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/$', planningView.planning, name='planning'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/protocol/$', planningView.protocol, name='protocol'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/quality/$', planningView.quality_assessment_checklist, name='quality_assessment_checklist'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/planning/extraction/$', planningView.data_extraction_form, name='data_extraction_form'),

    # Conducting Phase
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/$', conductingView.conducting, name='conducting'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/search/$', conductingView.search_studies, name='search_studies'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/import/$', conductingView.import_studies, name='import_studies'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/studies/$', conductingView.study_selection, name='study_selection'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/quality/$', conductingView.quality_assessment, name='quality_assessment'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/extraction/$', conductingView.data_extraction, name='data_extraction'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/conducting/analysis/$', conductingView.data_analysis, name='data_analysis'),

    # Reporting Phase
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/$', reportingView.reporting, name='reporting'),
    re_path(r'^(?P<username>[^/]+)/(?P<review_name>[^/]+)/reporting/export/$', reportingView.export, name='export'),

    # Review Settings
    re_path(r'^review_settings/transfer/$', settingsView.transfer, name='transfer_review'),
    re_path(r'^review_settings/delete/$', settingsView.delete, name='delete_review'),
]

'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
