from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import (
    HomeView,
    QuoteView,
)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^quote/$', QuoteView.as_view(), name='quote'),
)

urlpatterns += staticfiles_urlpatterns()
