from django.contrib import admin

from events.models import Event, League, EventSignUp

# Register your models here.
admin.site.register(League)
admin.site.register(Event)
admin.site.register(EventSignUp)
