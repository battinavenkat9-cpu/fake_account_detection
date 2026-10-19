from django.db import models

class AccountAnalysis(models.Model):
    username = models.CharField(max_length=80)
    followers = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    posts = models.PositiveIntegerField()
    account_age_days = models.PositiveIntegerField()
    bio_length = models.PositiveIntegerField(default=0)
    has_profile_picture = models.BooleanField(default=True)
    posts_per_day = models.FloatField(default=0)
    prediction = models.CharField(max_length=10)
    risk_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"@{self.username} — {self.prediction}"
