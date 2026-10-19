from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count, Avg
from .forms import AccountAnalysisForm
from .models import AccountAnalysis
from .ml.detector import predict_account


def home(request):
    form = AccountAnalysisForm()
    total = AccountAnalysis.objects.count()
    fake_count = AccountAnalysis.objects.filter(prediction="Fake").count()
    real_count = AccountAnalysis.objects.filter(prediction="Real").count()
    recent = AccountAnalysis.objects.all()[:5]
    return render(request, "detector/home.html", {"form": form, "total": total, "fake_count": fake_count, "real_count": real_count, "recent": recent})


def analyze(request):
    if request.method != "POST":
        return redirect("home")
    form = AccountAnalysisForm(request.POST)
    if not form.is_valid():
        total = AccountAnalysis.objects.count()
        return render(request, "detector/home.html", {"form": form, "total": total, "fake_count": AccountAnalysis.objects.filter(prediction="Fake").count(), "real_count": AccountAnalysis.objects.filter(prediction="Real").count(), "recent": AccountAnalysis.objects.all()[:5]})
    data = form.cleaned_data
    result = predict_account(followers=data["followers"], following=data["following"], posts=data["posts"], account_age_days=data["account_age_days"], bio_length=data.get("bio_length") or 0, has_profile_picture=data["has_profile_picture"] == "yes")
    analysis = AccountAnalysis.objects.create(username=data["username"], followers=data["followers"], following=data["following"], posts=data["posts"], account_age_days=data["account_age_days"], bio_length=data.get("bio_length") or 0, has_profile_picture=data["has_profile_picture"] == "yes", posts_per_day=result["features"]["posts_per_day"], prediction=result["prediction"], risk_score=result["risk_score"])
    return render(request, "detector/result.html", {"analysis": analysis, "result": result})


def history(request):
    records = AccountAnalysis.objects.all()
    return render(request, "detector/history.html", {"records": records, "total": records.count(), "fake_count": records.filter(prediction="Fake").count(), "real_count": records.filter(prediction="Real").count()})


def about(request):
    return render(request, "detector/about.html")
