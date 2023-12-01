from django.contrib.auth import get_user_model
from django.db import models

from events.models import Event
from teams.models import Team

User = get_user_model()

LEAGUE_TYPE_CHOICE = (

    ('Stripe', 'Stripe'),
    ('Paypal', 'Paypal'),
)
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  blank=True, related_name='user_payments')
    holder_name = models.CharField(max_length=255, blank=True, null=True)
    card_number = models.CharField(max_length=255, blank=True, null=True)
    expiry_month = models.CharField(max_length=255, blank=True, null=True)
    expiry_year = models.CharField(max_length=255, blank=True, null=True)
    cvc = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=255, choices=LEAGUE_TYPE_CHOICE, blank=True, null=True)

    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True, related_name='event_payments')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True, related_name='team_payments')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
