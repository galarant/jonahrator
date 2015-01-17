from __future__ import absolute_import

from django.conf.urls import patterns, include, url

from django.contrib import admin

from .views import (
    HomeView,
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
)
