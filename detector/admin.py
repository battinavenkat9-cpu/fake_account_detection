from django.contrib import admin
from .models import AccountAnalysis

@admin.register(AccountAnalysis)
class AccountAnalysisAdmin(admin.ModelAdmin):
    list_display = ("username", "prediction", "risk_score", "followers", "following", "created_at")
    list_filter = ("prediction", "has_profile_picture", "created_at")
    search_fields = ("username",)
