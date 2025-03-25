import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
django.setup()

from rest_framework.test import APIClient
from django.contrib.auth.models import User

# 初始化 client
client = APIClient()

# 確保使用者唯一
User.objects.filter(username='testuser').delete()
user = User.objects.create_user(username='testuser', password='testpass')

# 模擬登入
client.force_authenticate(user=user)

# 建立對話
res1 = client.post('/api/conversations/', {'user': user.id, 'status': 'pending'}, format='json')

if res1.status_code == 201:
    conversation_id = res1.json()['id']

    # 傳送訊息（第 1 則）
    client.post('/api/messages/', {
        'conversation': conversation_id,
        'role': 'user',
        'content': '你好 AI'
    }, format='json')

    # 傳送訊息（第 2 則）
    client.post('/api/messages/', {
        'conversation': conversation_id,
        'role': 'user',
        'content': '第二句話'
    }, format='json')

    # 查詢對話中的訊息（由新到舊）
    res3 = client.get(f'/api/messages/?conversation={conversation_id}&ordering=-timestamp')
    print("Get messages by descending timestamp:", res3.status_code)
    for m in res3.json():
        print(f"[{m['timestamp']}] {m['role']}: {m['content']}")

else:
    print("Create conversation failed!")


# import os
# import django

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
# django.setup()

# from rest_framework.test import APIClient
# from django.contrib.auth.models import User

# # 初始化 client
# client = APIClient()

# # 確保使用者唯一
# User.objects.filter(username='testuser').delete()
# user = User.objects.create_user(username='testuser', password='testpass')

# # 模擬登入
# client.force_authenticate(user=user)

# # 建立對話
# res1 = client.post('/api/conversations/', {
#     'status': 'pending'
# }, format='json')

# # res1 = client.post('/api/conversations/', {'status': 'pending'}, format='json')
# # print("Create conversation:", res1.status_code, res1.json())

# if res1.status_code == 201:
#     conversation_id = res1.json()['id']

#     # 傳送訊息
#     res2 = client.post('/api/messages/', {
#         'conversation': conversation_id,
#         'role': 'user',
#         'content': '你好 AI'
#     }, format='json')
#     print("Send message:", res2.status_code, res2.json())

#     # 查詢對話中的訊息
#     res3 = client.get('/api/messages/', {'conversation': conversation_id})
#     print("Get messages:", res3.status_code, res3.json())
# else:
#     print("Create conversation failed!")


# # import os
# # import django

# # # 在導入任何 Django 模組之前先設定
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

# # # 初始化 Django
# # django.setup()

# # from rest_framework.test import APIClient
# # from django.contrib.auth.models import User

# # client = APIClient()

# # # 建立使用者並登入
# # user = User.objects.create_user(username='testuser', password='testpass')
# # client.force_authenticate(user=user)

# # # 建立對話
# # res1 = client.post('/api/conversations/', {'status': 'pending'})
# # print("Create conversation:", res1.status_code, res1.data)

# # # 發送訊息
# # conversation_id = res1.data['id']
# # res2 = client.post('/api/messages/', {
# #     'conversation': conversation_id,
# #     'role': 'user',
# #     'content': 'Hello AI!'
# # })
# # print("Send message")
