from rest_framework import viewsets

from .serializers import *


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class CoordViewSet(viewsets.ModelViewSet):
    queryset = Coord.objects.all()
    serializer_class = CoordSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class PerevalImageViewSet(viewsets.ModelViewSet):
    queryset = PerevalImage.objects.all()
    serializer_class = PerevalImageSerializer


