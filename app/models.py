from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.conf import settings

# Create your models here.

CHAR_LIST  = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
)

# new AbstractUser model containing a friend_code
class User(AbstractUser):
    friend_code = models.CharField(max_length=20, unique=True)
    
    def assign_friend_code(self):
        if not self.friend_code:
            while True:
                base_code = "friend_code_"
                for i in range(0, 8):
                    random_index = random.randint(0, len(CHAR_LIST) - 1)
                    base_code += CHAR_LIST[random_index]
                if not User.objects.filter(friend_code=base_code).exists():
                    self.friend_code = base_code
                    break

    def __str__(self):
        return self.username

# chats of the specific user
class TextChat(models.Model):
    text = models.CharField(max_length=5000)
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sent_by')
    recieve_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recieve_by')
    sent_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'TextChats'
    
    def __str__(self):
        return 'Sent: ' + self.sent_by.username + ' Recieved: ' + self.recieve_by.username

# all the users a person has as friends 
class UserFriend(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendships')
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='added_by')
    
    def __str__(self):
        return 'USER: ' + self.user.username + ' FRIEND: ' + self.friend.username
