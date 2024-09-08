import random
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Match
from .api import get_current_user

def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


class MatchViewsets(viewsets.ViewSet):
    queryset = Match.objects.all()

    @action(methods=['GET'], detail=False, url_name='temp_room',url_path="temp_room")
    def get_temp_room(self,request):
        try:
            access_token = request.GET.get('access_token')
            if access_token:
                response = get_current_user(access_token)
                if response.get("id"):
                    matchs = self.queryset.filter(state="waiting")
                    if len(matchs) == 0:
                        match = Match.objects.create()
                        print(match)
                        return Response({"id": match.id}, status=status.HTTP_200_OK)
                    else:
                        match = random.choice(matchs)
                        return Response({"id": match.id}, status=status.HTTP_200_OK)
            return Response({"message": "user not found"}, status=status.HTTP_401_UNAUTHORIZED)

        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_401_UNAUTHORIZED)
