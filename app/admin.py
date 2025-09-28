from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserFriend, TextChat

admin.site.register(User, UserAdmin)
admin.site.register(UserFriend)
admin.site.register(TextChat)