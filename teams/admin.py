from django.contrib import admin

from teams.models import Team, TeamMember, TeamGallery, TeamSchedule, TeamLineUp


admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(TeamGallery)
admin.site.register(TeamSchedule)
admin.site.register(TeamLineUp)
