from django.contrib import admin

from teams.models import Team, TeamMember, TeamGallery, TeamSchedule, TeamLineUp, \
    TeamPlayerInviteEmail, TeamPlayerInvite

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(TeamGallery)
admin.site.register(TeamSchedule)
admin.site.register(TeamLineUp)
admin.site.register(TeamPlayerInvite)
admin.site.register(TeamPlayerInviteEmail)
