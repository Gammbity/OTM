from rest_framework.routers import DefaultRouter
from .views import StudentApiViewSet, StudentCreateApiViewSet, StudentDetApiView, StudentUpdateApiView, AddSponsorApiView, AddSponsorListApiView
from django.urls import path

urlpatterns = [
    path('student/', StudentApiViewSet.as_view({'get': 'list'})),
    path('student/<int:pk>/', StudentDetApiView.as_view()),
    path('student/update/<int:pk>/', StudentUpdateApiView.as_view()),
    path('student/create/', StudentCreateApiViewSet.as_view({'post': 'create'})),
    path('add/', AddSponsorApiView.as_view()),
    path('add/list', AddSponsorListApiView.as_view()),
]