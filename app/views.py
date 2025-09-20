from django.shortcuts import render, reverse
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import *
from django.shortcuts import redirect 
from django.contrib.auth import login, authenticate
from .models import *
from django.db.models import Q

# Create your views here.

#homepage 
@method_decorator(login_required, name='dispatch')
class IndexView(View):
    def get(self, request, *args, **kwargs):
        chats = UserChat.objects.filter(user=request.user)
        context = {
            'chats': chats
        }
        return render(request, 'chats/index.html', context)


# registeration 
class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'chats/register.html', context)
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            context = {
                'form': form
            }
            return render(request, 'chats/register.html', context)


# login
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form
        }
        return render(request, 'chats/login.html', context)
    
    def post(self, request):
        success_url = reverse('chats:index')
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(success_url)
            else:
                form.add_error(None, 'Invalid Credentials!')
        return render(request, 'chats/login.html', {'form': form})

class ChatTextView(View):
    def get(self, request, pk):
        friend = User.objects.get(pk=pk)
        chats = TextChat.objects.filter(Q(sent_by=request.user, recieve_by=friend) | Q(sent_by=friend, recieve_by=request.user)).order_by('sent_at')
        print(chats)
        context = {
            'chats': chats,
            'friend_username': friend.username
        }
        return render(request, 'chats/chat_text.html', context)
