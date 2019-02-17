# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import *


def home(request):
    """
    This method is to render home page with team detail.
    :param request:
    :return:
    """
    teams = Team.objects.all()
    return render(request, 'home.html', {'teams': teams})


def matches(request):
    """
    This method render match detail.
    :param request:
    :return:
    """
    matches = Matches.objects.all()
    return render(request, 'matches.html', {'matches': matches})


def players(request, id):
    """
    This method render player page.
    :param request:
    :param id:
    :return:
    """
    tm = Team.objects.get(id=id)
    players = Player.objects.filter(team=id)

    return render(request, 'players.html', {'players': players, 'team_name': tm.name})


def player_history(request, id):
    """
    This view is to render player history.
    :param request:
    :param id:
    :return:
    """
    obj = PlayerMatch.objects.filter(player=id)
    player = Player.objects.get(id=id)
    match_played= obj.count()
    total_runs = 0
    fifty = 0
    hundred = 0
    highest = 0
    for i in obj:
        total_runs += i.run
        if i.run > highest:
            highest = i.run
        if i.run >= 50:
            fifty += 1
        if i.run >= 100:
            hundred += 1

    return render(request, 'player_history.html', {'match_played': match_played, 'total_runs': total_runs,
                                                   'fifty': fifty, 'hundred': hundred, 'highest': highest, 'player': player})


def point_table(request):
    """
    This view if to render point table page.
    :param request:
    :return:
    """
    points = Point.objects.all()
    return render(request, 'point_table.html', {'points': points})