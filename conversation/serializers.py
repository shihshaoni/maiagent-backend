from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        read_only_fields = ['user']


# from rest_framework import serializers
# from .models import Conversation, Message

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = "__all__"

# class ConversationSerializer(serializers.ModelSerializer):
#     messages = MessageSerializer(many=True, read_only=True)

#     class Meta:
#         model = Conversation
#         fields = "__all__"


# from rest_framework import serializers
# from .models import Conversation, Message

# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ["id", "role", "content", "timestamp"]

# class ConversationSerializer(serializers.ModelSerializer):
#     messages = MessageSerializer(many=True, read_only=True)

#     class Meta:
#         model = Conversation
#         fields = ["id", "user", "status", "created_at", "updated_at", "messages"]