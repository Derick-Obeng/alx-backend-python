

from rest_framework.pagination import PageNumberPagination

class MessagePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'  # Optional: allow dynamic size via ?page_size=xxx
    max_page_size = 100
