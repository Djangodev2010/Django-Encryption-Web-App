from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChatSerializer
from app.models import TextChat

@api_view(['GET'])
def getChat(request):
    chats = TextChat.objects.all()
    serializer = ChatSerializer(chats, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addChat(request):
    chat = ChatSerializer(data=request.data)
    if chat.is_valid():
        chat.save()
    return Response(chat.data)


