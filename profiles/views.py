import json
from django.http import HttpResponse
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['POST'])
def register(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        print(serialized.init_data['first_name'])
        print(serialized.init_data['last_name'])
        user = User.objects.create_user(
                   serialized.init_data['email'],
                   serialized.init_data['username'],
                   serialized.init_data['password'])
        user.first_name = serialized.init_data['first_name']
        user.last_name = serialized.init_data['last_name']
        user.save()
        data = {'token': Token.objects.get(user=user).key}
        return HttpResponse(json.dumps(data), content_type='application/json',
                            status=status.HTTP_201_CREATED)
    else:
        return HttpResponse(serialized._errors, content_type='application/json',
                            status=status.HTTP_400_BAD_REQUEST)