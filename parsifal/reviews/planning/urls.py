# coding: utf-8

from django.urls import path,re_path,include
from . import views

app_name='reviews.planning'
urlpatterns = [
    re_path(r'^save_source/$', views.save_source, name='save_source'),
    re_path(r'^remove_source/$', views.remove_source_from_review, name='remove_source_from_review'),
    re_path(r'^suggested_sources/$', views.suggested_sources, name='suggested_sources'),
    re_path(r'^add_suggested_sources/$', views.add_suggested_sources, name='add_suggested_sources'),
    re_path(r'^save_question/$', views.save_question, name='save_question'),
    re_path(r'^save_question_order/$', views.save_question_order, name='save_question_order'),
    re_path(r'^save_picoc/$', views.save_picoc, name='save_picoc'),
    re_path(r'^add_or_edit_question/$', views.add_or_edit_question, name='add_or_edit_question'),
    re_path(r'^remove_question/$', views.remove_question, name='remove_question'),
    re_path(r'^save_objective/$', views.save_objective, name='save_objective'),
    re_path(r'^add_criteria/$', views.add_criteria, name='add_criteria'),
    re_path(r'^remove_criteria/$', views.remove_criteria, name='remove_criteria'),

    re_path(r'^import_pico_keywords/$', views.import_pico_keywords, name='import_pico_keywords'),
    re_path(r'^add_keyword/$', views.add_keyword, name='add_keyword'),
    re_path(r'^edit_keyword/$', views.edit_keyword, name='edit_keyword'),
    re_path(r'^remove_keyword/$', views.remove_keyword, name='remove_keyword'),

    re_path(r'^add_quality_assessment_question/$', views.add_quality_assessment_question, name='add_quality_assessment_question'),
    re_path(r'^edit_quality_assessment_question/$', views.edit_quality_assessment_question, name='edit_quality_assessment_question'),
    re_path(r'^save_quality_assessment_question/$', views.save_quality_assessment_question, name='save_quality_assessment_question'),
    re_path(r'^save_quality_assessment_question_order/$', views.save_quality_assessment_question_order, name='save_quality_assessment_question_order'),
    re_path(r'^remove_quality_assessment_question/$', views.remove_quality_assessment_question, name='remove_quality_assessment_question'),
    re_path(r'^add_quality_assessment_answer/$', views.add_quality_assessment_answer, name='add_quality_assessment_answer'),
    re_path(r'^edit_quality_assessment_answer/$', views.edit_quality_assessment_answer, name='edit_quality_assessment_answer'),
    re_path(r'^save_quality_assessment_answer/$', views.save_quality_assessment_answer, name='save_quality_assessment_answer'),
    re_path(r'^remove_quality_assessment_answer/$', views.remove_quality_assessment_answer, name='remove_quality_assessment_answer'),
    re_path(r'^add_suggested_answer/$', views.add_suggested_answer, name='add_suggested_answer'),
    re_path(r'^add_new_data_extraction_field/$', views.add_new_data_extraction_field, name='add_new_data_extraction_field'),
    re_path(r'^edit_data_extraction_field/$', views.edit_data_extraction_field, name='edit_data_extraction_field'),
    re_path(r'^save_data_extraction_field/$', views.save_data_extraction_field, name='save_data_extraction_field'),
    re_path(r'^save_data_extraction_field_order/$', views.save_data_extraction_field_order, name='save_data_extraction_field_order'),
    re_path(r'^remove_data_extraction_field/$', views.remove_data_extraction_field, name='remove_data_extraction_field'),
    re_path(r'^calculate_max_score/$', views.calculate_max_score, name='calculate_max_score'),
    re_path(r'^save_cutoff_score/$', views.save_cutoff_score, name='save_cutoff_score'),
    re_path(r'^generate_search_string/$', views.generate_search_string, name='generate_search_string'),
    re_path(r'^save_generic_search_string/$', views.save_generic_search_string, name='save_generic_search_string'),
]
