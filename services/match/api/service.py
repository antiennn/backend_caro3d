from .models import Match

def chang_state_start_game(chat_room):
    temp_room = Match.objects.get(id=chat_room)
    temp_room.state = "playing"
