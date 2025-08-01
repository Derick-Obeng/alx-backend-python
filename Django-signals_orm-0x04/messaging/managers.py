from .models import models, UnreadMessagesManager


class UnreadMessagesManager(models.Manager):

    def for_user(self, user):
        return self.filter(receiver=user, read=False).only('id', 'content', 'timestamp', 'sender')

    objects = models.Manager()
    unread = UnreadMessagesManager()
