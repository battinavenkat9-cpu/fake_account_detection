from django.contrib import admin
from django.urls import path
from detector import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('home/',views.home,name='home'),
    path('analyze/',views.analyze,name='analyze'),
    path('history/',views.history,name='history'),
    path('about/',views.about,name='about'),
]
