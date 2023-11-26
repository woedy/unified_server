from django.contrib import admin

from events.models import Event, League

# Register your models here.
admin.site.register(League)
admin.site.register(Event)
