from django.db import models
from django.contrib.auth.models import AbstractUser
import random
from django.conf import settings

# Create your models here.

# the char list for setting a unique friend_code for the user
CHAR_LIST  = list(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz"
    "0123456789"
    "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~\\"
)

# custom user model for incorporating a friend_code field for sending friend requests
class User(AbstractUser):
    friend_code = models.CharField(max_length=20, unique=True)
    
    # a method that first checks if a friend_code is assigned or not
    # if the friend_code is not assigned, then it sets a new and unique friend_code
    def assign_friend_code(self):
        if not self.friend_code:
            while True:
                base_code = "friend_code_"
                # the loop to add 8 random and unique letters to the base_code
                for i in range(0, 8):
                    # selecting a random index
                    random_index = random.randint(0, len(CHAR_LIST) - 1)
                    # concatenating a new char to the base_code
                    base_code += CHAR_LIST[random_index]
                if not User.objects.filter(friend_code=base_code).exists():
                    self.friend_code = base_code
                    break

    def __str__(self):
        return self.username

# a model for chats of a specific user
class TextChat(models.Model):
    # the text of a chat
    text = models.CharField(max_length=5000)
    # this field is for who sent the chat
    sent_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='sent_by')
    # this field is for who recieved the chat
    recieve_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recieve_by')
    # this field is to keep track of the time the message was sent
    sent_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'TextChats'
    
    def __str__(self):
        return 'Sent: ' + self.sent_by.username + ' Recieved: ' + self.recieve_by.username

# all the users a person has as friends or requests
class UserFriend(models.Model):
    # the user that's logged in
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friendships')
    # the friend that the user has relation with
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='added_by')
    # a name field storing the name of the friend for easier db query
    name = models.CharField(max_length=500)
    # a BooleanField for checking if the friend is a request or accepted by the user
    is_request = models.BooleanField(default=True)
    # a created_at field to keep records of the requests
    created_at = models.DateTimeField(auto_now_add=True)
    
    # a method to automatically set the name of the request 
    def set_username(self):
        if not self.name:
            self.name = self.friend.username
            return self.name
    
    def __str__(self):
        return "User: " + self.user.username + " Friend: " + self.name
