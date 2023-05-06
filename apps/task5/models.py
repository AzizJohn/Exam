from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Country(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    flag = models.ImageField(upload_to="country", verbose_name=_("Flag"), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class League(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("Country"), null=True, blank=True)
    logo = models.ImageField(upload_to="league", verbose_name=_("Logo"), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("League")
        verbose_name_plural = _("Leagues")


class Team(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    symbol = models.ImageField(upload_to="team", verbose_name=_("Symbol"), null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("Country"), null=True, blank=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name=_("League"), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")


class Match(TimeStampedModel):
    match_time = models.TimeField(verbose_name=_("Time"))
    match_date = models.DateField(verbose_name=_("Date"))
    host = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Host"), related_name="host")
    guest = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Guest"), related_name="guest")
    stadium = models.CharField(max_length=255, verbose_name=_("Stadium"))

    is_favourite = models.BooleanField(default=False, verbose_name=_("Is Favourite"))
    is_finished = models.BooleanField(default=False, verbose_name=_("Is Finished"))

    def __str__(self):
        return f'{self.host} - {self.guest}'

    class Meta:
        verbose_name = _("Match")
        verbose_name_plural = _("Matches")


class Score(TimeStampedModel):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, verbose_name=_("Match"), null=True, blank=True)
    host_score = models.IntegerField(verbose_name=_("Host Score"), null=True, blank=True)
    guest_score = models.IntegerField(verbose_name=_("Guest Score"), null=True, blank=True)

    def __str__(self):
        return f'{self.host_score} - {self.guest_score}'

    class Meta:
        verbose_name = _("Score")
        verbose_name_plural = _("Scores")


class Round(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    league = models.ForeignKey(League, on_delete=models.CASCADE, verbose_name=_("League"), null=True, blank=True)
    matches = models.ManyToManyField(Match, verbose_name=_("Matches"),)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Round")
        verbose_name_plural = _("Rounds")


class Player(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    surname = models.CharField(max_length=255, verbose_name=_("Surname"))
    birth_date = models.DateField(verbose_name=_("Birth Date"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("Country"), null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name=_("Team"), null=True, blank=True)
    number = models.IntegerField(verbose_name=_("Number"), null=True, blank=True)
    position = models.CharField(max_length=255, verbose_name=_("Position"), null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.team}'

    class Meta:
        verbose_name = _("Player")
        verbose_name_plural = _("Players")


class Referee(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    surname = models.CharField(max_length=255, verbose_name=_("Surname"))
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name=_("Country"), null=True, blank=True)
    position = models.CharField(max_length=255, verbose_name=_("Position"), null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _("Referee")
        verbose_name_plural = _("Referees")
