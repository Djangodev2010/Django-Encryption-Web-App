from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='view'),
    path('register', RegisterView.as_view(), name='register'),
    
    
]

