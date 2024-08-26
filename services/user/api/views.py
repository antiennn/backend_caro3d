import requests
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    @action(methods=['GET'], detail=False, url_name='create_post')
    def auth(self,request):
        try:
            access_token = request.headers.get('Authorization').split()[1]
            if access_token:
                response = requests.get("https://graph.facebook.com/me?access_token=" + access_token).json()
                if response.get("name"):
                    temp_user, isCreated = User.objects.get_or_create(
                        display_name=response.get("name"),
                        id=response.get("id"),
                    )
                    print(temp_user)
                    return Response(UserSerializer(temp_user).data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)