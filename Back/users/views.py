from xmlrpc.client import ResponseError
from rest_framework import viewsets, permissions, mixins
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .serializers import USERSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from django.http import HttpResponse

class USERViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = USERSerializer

    def create(self, request):
        try:
            username = json.loads(request.body)['username']
            password = json.loads(request.body)['password']

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response("Usuario no existe", status=status.HTTP_404_NOT_FOUND)

            pwd_valid = check_password(password, user.password)
            if(not pwd_valid):
                return Response("Contrasena Invalida",status=status.HTTP_400_BAD_REQUEST)

            token, _ = Token.objects.get_or_create(user=user)
            response = {
                "user" : user.username,
                "token" : token.key
            }
            return HttpResponse(json.dumps(response), content_type="application/json")
        except:
            return Response("A otro con se hueso mijo >:v",status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
