from rest_framework import viewsets
from .serializers import PeopleSerializer
from .models import People


class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all().order_by('fio')
    serializer_class = PeopleSerializer
