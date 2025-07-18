from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Conversation, Message, CustomUser
from .serializers import (
    UserSerializer,
    ConversationSerializer,
    MessageSerializer
)


class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer


    filter_backends = [filters.SearchFilter]
    search_fields = ['participants__username']

    def get_queryset(self):
        # Only show conversations the current user is a participant in
        return self.queryset.filter(participants=self.request.user)

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.participants.add(self.request.user)
        conversation.save()


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]


    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['text', 'sender__username']  # Adjust field name to your model
    ordering_fields = ['timestamp']  # Adjust field name to your model

    def get_queryset(self):
        # Only show messages in conversations the user is part of
        return self.queryset.filter(conversation__participants=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
