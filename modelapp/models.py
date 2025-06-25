from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CataractScan(models.Model):
    DIAGNOSIS_CHOICES = [
        ('normal eye', 'Normal Eye'),
        ('immature cataract', 'Immature Cataract'),
        ('mature cataract', 'Mature Cataract'),
        ('error', 'Error – No Classification'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='scans/')
    diagnosis = models.CharField(max_length=30, choices=DIAGNOSIS_CHOICES)
    confidence = models.FloatField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} - {self.diagnosis} ({self.confidence:.1%})"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
