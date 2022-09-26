from .models import MASTER, ROLE, CITY, ENTITY
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import MASTERSerializer

class MASTERViewSets(viewsets.ModelViewSet):
    queryset = MASTER.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MASTERSerializer