from django.shortcuts import render


from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ReadOnlyModelViewSet

from messaging_app.chats.serializers import MessageSerializer
from .models import Message
from django.db.models import Prefetch
from django.http import JsonResponse
from .utils import get_threaded_replies
from .models import Message
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




User = get_user_model()

@csrf_exempt
def delete_user(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return JsonResponse({"message": "User deleted successfully."})
    return JsonResponse({"error": "Only POST allowed"}, status=405)

root_messages = Message.objects.filter(parent_message__isnull=True).select_related(
    'sender', 'receiver'
).prefetch_related(
    Prefetch('replies', queryset=Message.objects.select_related('sender'))
)

def threaded_conversation_view(request, message_id):
    try:
        root = Message.objects.select_related('sender').prefetch_related('replies__sender').get(id=message_id)
        data = {
            'id': root.id,
            'sender': root.sender.username,
            'content': root.content,
            'timestamp': root.timestamp,
            'replies': get_threaded_replies(root)
        }
        return JsonResponse(data)
    except Message.DoesNotExist:
        return JsonResponse({'error': 'Message not found'}, status=404)


@login_required
def unread_messages_view(request):
    unread_msgs = Message.unread.unread.for_user(request.user)
    sender = request.user
    return render(request, 'messaging/unread_messages.html', {'messages': unread_msgs})

@method_decorator(cache_page(60), name='list')  # 60 seconds cache
class MessageViewSet(ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer