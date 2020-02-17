# coding: utf-8

from django.urls import path,re_path,include
from . import views

app_name = 'reviews.conducting'
urlpatterns = [
    re_path(r'^add_source_string/$', views.add_source_string, name='add_source_string'),
    re_path(r'^save_source_string/$', views.save_source_string, name='save_source_string'),
    re_path(r'^remove_source_string/$', views.remove_source_string, name='remove_source_string'),
    re_path(r'^import_base_string/$', views.import_base_string, name='import_base_string'),
    re_path(r'^search_scopus/$', views.search_scopus, name='search_scopus'),
    re_path(r'^search_science_direct/$', views.search_science_direct, name='search_science_direct'),
    re_path(r'^new_article/$', views.new_article, name='new_article'),
    re_path(r'^import/bibtex_file/$', views.import_bibtex, name='import_bibtex'),
    re_path(r'^import/bibtex_raw_content/$', views.import_bibtex_raw_content, name='import_bibtex_raw_content'),
    re_path(r'^source_articles/$', views.source_articles, name='source_articles'),
    re_path(r'^article_details/$', views.article_details, name='article_details'),
    re_path(r'^find_duplicates/$', views.find_duplicates, name='find_duplicates'),
    re_path(r'^resolve_duplicated/$', views.resolve_duplicated, name='resolve_duplicated'),
    re_path(r'^export_results/$', views.export_results, name='export_results'),
    re_path(r'^resolve_all/$', views.resolve_all, name='resolve_all'),
    re_path(r'^save_article_details/$', views.save_article_details, name='save_article_details'),
    re_path(r'^save_quality_assessment/$', views.save_quality_assessment, name='save_quality_assessment'),
    re_path(r'^quality_assessment_detailed/$', views.quality_assessment_detailed, name='quality_assessment_detailed'),
    re_path(r'^quality_assessment_summary/$', views.quality_assessment_summary, name='quality_assessment_summary'),
    re_path(r'^multiple_articles_action/remove/$', views.multiple_articles_action_remove, name='multiple_articles_action_remove'),
    re_path(r'^multiple_articles_action/accept/$', views.multiple_articles_action_accept, name='multiple_articles_action_accept'),
    re_path(r'^multiple_articles_action/reject/$', views.multiple_articles_action_reject, name='multiple_articles_action_reject'),
    re_path(r'^multiple_articles_action/duplicated/$', views.multiple_articles_action_duplicated, name='multiple_articles_action_duplicated'),
    #re_path(r'^articles/upload/$', 'articles_upload', name='articles_upload'),
    re_path(r'^save_data_extraction/$', views.save_data_extraction, name='save_data_extraction'),
    re_path(r'^save_data_extraction_status/$', views.save_data_extraction_status, name='save_data_extraction_status'),
    re_path(r'^articles_selection_chart/$', views.articles_selection_chart, name='articles_selection_chart'),
    re_path(r'^articles_per_year/$', views.articles_per_year, name='articles_per_year'),
    re_path(r'^export_data_extraction/$', views.export_data_extraction, name='export_data_extraction')
]
