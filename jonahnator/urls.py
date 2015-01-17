from __future__ import absolute_import

from django.conf.urls import patterns, include, url

from .views import (
    HomeView,
    QuoteView,
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^quote/$', QuoteView.as_view(), name='quote'),
)
