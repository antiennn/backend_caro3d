import requests
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from .api import get_access_token
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    @action(methods=['GET'], detail=False, url_name='create_user')
    def auth(self,request):
        try:
            access_token = request.GET.get('access_token')
            if access_token:
                response = get_access_token(access_token)
                if response.get("name"):
                    temp_user, isCreated = User.objects.get_or_create(
                        display_name=response.get("name"),
                        id=response.get("id"),
                    )
                    return Response(UserSerializer(temp_user).data, status=status.HTTP_200_OK)
            return Response({"message": "user not found"}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)


