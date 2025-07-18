

from rest_framework import serializers
from .models import CustomUser, Conversation, Message

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'avatar', 'is_online']


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'sender_username', 'message_body', 'sent_at', 'is_read']

class ConversationSerializer(serializers.ModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    messages = MessageSerializer(many=True, read_only=True)
    message_count = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'participants', 'created_at', 'messages', 'message_count']

    def get_message_count(self, obj):
        return obj.messages.count()

    def validate(self, data):
        if 'message_body' in data and len(data['message_body']) < 1:
            raise serializers.ValidationError("Message body can't be empty.")
        return data

