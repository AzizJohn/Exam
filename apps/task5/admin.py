from django.contrib import admin

# Register your models here.

from apps.task5.models import Country, League, Team, Match, Player, Referee, Round, Score
admin.site.register(Country)
admin.site.register(League)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Player)
admin.site.register(Referee)
admin.site.register(Round)
admin.site.register(Score)
