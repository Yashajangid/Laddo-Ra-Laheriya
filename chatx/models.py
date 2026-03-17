from django.db import models
from django.conf import settings
from gigs.models import Gig

class ChatMessage(models.Model):
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
