from django.conf.urls import url, include
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^$', home),
    url(r'^matches/$', matches),
    url(r'^players/(?P<id>[a-zA-Z0-9]{0,30})/$', players),
    url(r'^player-history/(?P<id>[a-zA-Z0-9]{0,30})/$', player_history),
    url(r'^point-table/$', point_table),
    ]


