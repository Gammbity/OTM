from .models import StudentModel, AddSponsorModel
from .serializers import StudentSerializer, AddSponsorListSerializer, AddSponsorSerializer, StudentCreateSerializer, StudentDetSerializer, StudentUpdateSerializer
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import generics

class StudentApiViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [IsAuthenticated]

class StudentCreateApiViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentCreateSerializer
    # permission_classes = [IsAuthenticated]

class StudentDetApiView(generics.RetrieveDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentDetSerializer


class StudentUpdateApiView(generics.UpdateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentUpdateSerializer

class AddSponsorListApiView(generics.ListAPIView):
    queryset = AddSponsorModel.objects.all()
    serializer_class = AddSponsorListSerializer

class AddSponsorApiView(generics.CreateAPIView):
    queryset = AddSponsorModel.objects.all()
    serializer_class = AddSponsorSerializer
