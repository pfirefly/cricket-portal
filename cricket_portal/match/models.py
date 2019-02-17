# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    """
    This model defines team structure.
    """
    name = models.CharField(max_length=100)
    club_state = models.CharField(max_length=50)
    logo = models.ImageField()

    def __str__(self):
        return self.name


class Player(models.Model):
    """
    This model to define player structure.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="media/")
    jersey_number = models.IntegerField()
    country = models.CharField(max_length=100)
    team = models.ForeignKey(Team)

    def __str__(self):
        return self.first_name


class Matches(models.Model):
    """
    This model to define matches structure.
    """
    team1 = models.ForeignKey(Team, related_name='team1')
    team2 = models.ForeignKey(Team, related_name='team2')
    winner = models.ForeignKey(Team)
    date = models.DateField()

    def __str__(self):
        return '%s Vs %s' %(self.team1, self.team2)


class PlayerMatch(models.Model):
    """
    This model to define player match structure.
    """
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Matches)
    run = models.IntegerField()

    def __str__(self):
        return str(self.match)


class Point(models.Model):
    """
    This model to define point table structure.
    """
    team = models.ForeignKey(Team, null=True, blank=True)
    point = models.IntegerField(default=0)

    def __str__(self):
        return str(self.point)