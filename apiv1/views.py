from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blacklist.models import BlackUrl
from .serializers import BlackUrlSerializer


class BlackUrlViewSet(viewsets.ModelViewSet):

    queryset = BlackUrl.objects.all()
    serializer_class = BlackUrlSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
