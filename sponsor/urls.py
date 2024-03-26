from django.urls import path
from .views import SponsorListApiView, SponsorDetApiView, SponsorUpdateApiView, SponsorCreateApiView

urlpatterns = [
    path('sponsor/', SponsorListApiView.as_view()),
    path('sponsor/create/', SponsorCreateApiView.as_view()),
    path('sponsor/<int:pk>/', SponsorDetApiView.as_view()),
    path('sponsor/update/<int:pk>/', SponsorUpdateApiView.as_view()),
]
