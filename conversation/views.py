from rest_framework import viewsets, permissions, filters
from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



# class ConversationViewSet(viewsets.ModelViewSet):
#     queryset = Conversation.objects.all()
#     serializer_class = ConversationSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        if message.role == "user":
            # Create auto-reply message
            Message.objects.create(
                conversation=message.conversation,
                role="ai",
                content="這是自動回覆：你好，有什麼我可以幫忙的嗎？"
            )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]  # 或依照你的權限需求修改
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'role']
    ordering_fields = ['timestamp']
    ordering = ['timestamp']  # 預設時間排序

    def get_queryset(self):
        queryset = super().get_queryset()
        conversation_id = self.request.query_params.get('conversation')
        if conversation_id:
            queryset = queryset.filter(conversation_id=conversation_id)
        return queryset
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content', 'role']

    from rest_framework import viewsets, filters  # 確保這行有加上 filters

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['timestamp']  # 允許用戶排序的欄位
    ordering = ['timestamp']  # 預設排序（升序）

    def get_queryset(self):
        queryset = super().get_queryset()
        conversation_id = self.request.query_params.get('conversation')
        if conversation_id:
            queryset = queryset.filter(conversation_id=conversation_id)
        return queryset
