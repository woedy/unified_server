from django.contrib import admin

from leaderboards.models import Standing, LeaderBoard, Award

admin.site.register(Standing)
admin.site.register(LeaderBoard)
admin.site.register(Award)
