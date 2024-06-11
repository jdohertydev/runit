from django.db import models

class ContactMessage(models.Model):
    """
    Model representing a contact message.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} ({self.email})'
