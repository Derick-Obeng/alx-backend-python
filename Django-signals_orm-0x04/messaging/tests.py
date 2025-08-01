from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Message, Notification

User = get_user_model()

class MessageNotificationSignalTest(TestCase):
    def test_notification_created_on_new_message(self):
        sender = User.objects.create_user(username='sender', password='pass')
        receiver = User.objects.create_user(username='receiver', password='pass')

        message = Message.objects.create(
            sender=sender,
            receiver=receiver,
            content='Hello!'
        )

        self.assertEqual(Notification.objects.count(), 1)
        self.assertEqual(Notification.objects.first().user, receiver)
