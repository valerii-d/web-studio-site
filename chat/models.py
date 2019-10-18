from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    user=models.ForeignKey(User,related_name='messages', on_delete=models.CASCADE)
    message=models.TextField(max_length=3000)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="messages"

    def __str__(self):
        return self.message

class Chat(models.Model):
    users=models.ManyToManyField(User,related_name='chat_users',blank=True)
    messages=models.ManyToManyField(Message,blank=True)

    class Meta:
        db_table="chats"

    def __str__(self):
        return "{}".format(self.pk) 