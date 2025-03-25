from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed")
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Conversation #{self.id} - {self.user.username}"

class Message(models.Model):
    ROLE_CHOICES = [
        ("user", "User"),
        ("ai", "AI")
    ]
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.role}] {self.content[:30]}"


# from django.db import models

# # Create your models here.

# # from django.conf import settings
# from django.contrib.auth.models import User


# class Conversation(models.Model):
#     STATUS_CHOICES = [
#         ("pending", "Pending"),
#         ("completed", "Completed")
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Message(models.Model):
#     ROLE_CHOICES = [
#         ("user", "User"),
#         ("ai", "AI")
#     ]
#     conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
#     role = models.CharField(max_length=10, choices=ROLE_CHOICES)
#     content = models.TextField()
#     timestamp = models.DateTimeField(auto_now_add=True)

