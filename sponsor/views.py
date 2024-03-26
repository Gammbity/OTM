from .models import SponsorModel
from .serializers import SponsorSerializers, SponsorDetSerializers, SponsorUpdateSerializers, SponsorCreateSerializers
from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend

class SponsorListApiView(generics.ListAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorSerializers
    # permission_classes = [IsAuthenticated]

class SponsorCreateApiView(generics.CreateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorCreateSerializers
    # permission_classes = [IsAuthenticated]

class SponsorDetApiView(generics.RetrieveDestroyAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorDetSerializers

class SponsorUpdateApiView(generics.UpdateAPIView):
    queryset = SponsorModel.objects.all()
    serializer_class = SponsorUpdateSerializers
