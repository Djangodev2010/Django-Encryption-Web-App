from rest_framework import serializers
from app.models import TextChat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextChat
        fields = '__all__'
