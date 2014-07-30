from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
