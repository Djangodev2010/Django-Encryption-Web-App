from django.db import models
from django.contrib.auth.models import AbstractUser
import random 

# Create your models here.

CHAR_LIST  = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
)

class User(AbstractUser):
    friend_code = models.CharField(max_length=20)
    
    def assign_friend_code(self):
        if not self.friend_code:
            base_code = "friend_code_"
            for i in range(0, len(CHAR_LIST)):
                pass

# chats of the specific user
class TextChat(models.Model):
    text = models.CharField(max_length=5000)
    sent_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='sent_by')
    recieve_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieve_by')
    sent_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'TextChats'
    
    def __str__(self):
        return 'Sent: ' + self.sent_by.username + ' Recieved: ' + self.recieve_by.username

# all the users a person has as friends 
class UserFriend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    
    def __str__(self):
        return 'USER: ' + self.user.username + ' FRIEND: ' + self.friend.username
