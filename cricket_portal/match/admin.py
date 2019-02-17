# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *


class TeamAdmin(admin.ModelAdmin):
    fields = ('name', 'club_state', 'logo')
    list_display = fields


class PlayerAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'jersey_number', 'country', 'team', 'profile_image')
    list_display = fields


class MatchesAdmin(admin.ModelAdmin):
    fields = ('team1', 'team2', 'winner', 'date')
    list_display = fields

class PlayerMatchAdmin(admin.ModelAdmin):
    fields = ('player', 'match', 'run')
    list_display = fields

class PointAdmin(admin.ModelAdmin):
    fields = ('team', 'point')
    list_display = fields

admin.site.register(Team, TeamAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Matches, MatchesAdmin)
admin.site.register(PlayerMatch, PlayerMatchAdmin)
admin.site.register(Point, PointAdmin)

