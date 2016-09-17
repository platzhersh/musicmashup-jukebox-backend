# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import utils
from api import views


jukebox = [
    url(r'^rooms/?$', utils.get_listview('jukebox', 'Room').as_view(), name="eventcategories"),
    url(r'^rooms/(?P<pk>[0-9]+)/?$', utils.get_retrieveview('jukebox', 'Room').as_view(), name='eventcategory'),

    url(r'^videos/?$', utils.get_listview('jukebox', 'Video').as_view(), name="videos"),
    url(r'^videos/(?P<pk>[0-9]+)/?$', utils.get_retrieveview('jukebox', 'Video').as_view(), name='video'),

]

# where it all comes together
urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^jukebox/', include(jukebox, namespace="jukebox")),
]

urlpatterns = format_suffix_patterns(urlpatterns)