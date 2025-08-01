
def get_threaded_replies(message):
    replies = []
    for reply in message.replies.all():
        nested = get_threaded_replies(reply)
        replies.append({
            'id': reply.id,
            'sender': reply.sender.username,
            'content': reply.content,
            'timestamp': reply.timestamp,
            'replies': nested
        })
    return replies