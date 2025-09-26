from django.urls import path
from .views import *

app_name = 'chats'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('<int:pk>/', ChatTextView.as_view(), name='chat_text'),
    path('send/<int:friendId>', SendMessage.as_view(), name='send_message')
    
    
]

