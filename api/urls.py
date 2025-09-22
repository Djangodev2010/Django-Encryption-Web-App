from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.getChat, name='getChat'),
    path('add/', views.addChat, name='addChat')
]

