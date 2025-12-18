from django.urls import path
from . import views

urlpatterns = [
    path("<str:day>", views.days_week)
]
