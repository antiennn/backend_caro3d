from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


class RoomNameViewsets(viewsets.ViewSet):
    @action(methods=['GET'], detail=False, url_name='temp_room')
    def temp_room(self,request):
        channel_layer = get_channel_layer()
        rooms = database_sync_to_async(channel_layer)
        print(channel_layer)
        return Response({"rooms": channel_layer})
