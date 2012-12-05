# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from {{ project_name }}.core import views


urlpatterns = patterns('',
    url(r'^$', views.index, name='core-index'),
)
