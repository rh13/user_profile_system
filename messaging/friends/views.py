from django.shortcuts import render, redirect
from accounts.models import UserProfile
from django.contrib.auth.models import User
from .models import Friend
# Create your views here.

def home(request):
    return render(request, 'home.html')


def view_user_profile(request, username):
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    args={'user': user}
    return render(request, 'friends/view_user_profile.html', args)

def friend_list(request):
    users = User.objects.exclude(username=request.user.username)
    friend= None
    try:
        friend = Friend.objects.get(current_user=request.user)
    except Friend.DoesNotExist:
        friend = Friend.objects.create(current_user=request.user)
    friends = friend.users.all()
    context = {'users': users, 'friends': friends}
    return render(request, 'friends/friend_list.html', context)


def change_friend(request, operation, username):
    new_friend= User.objects.get(username=username)
    if operation == 'add':
        Friend.make_friend(request.user,new_friend)
    elif operation== 'remove':
        Friend.unfriend(request.user,new_friend)
    return redirect('friend_list')
