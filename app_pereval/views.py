from rest_framework import viewsets
from rest_framework.response import Response

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

    def partial_update(self, request, *args, **kwargs):
        pereval = self.get_object()
        if pereval.status == 'new':
            serializer = PerevalSerializer(pereval, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'state': 1, 'message': 'Запись успешно изменена'})
            else:
                return Response({'state': 0, 'message': serializer.errors})
        else:
            return Response({'state': 0,
                             'message': f'Изменения не могут быть сохранены про причине: '
                                        f'{pereval.get_status_display()}'})


class PerevalImageViewSet(viewsets.ModelViewSet):
    queryset = PerevalImage.objects.all()
    serializer_class = PerevalImageSerializer


