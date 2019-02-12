from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, Http404
from message.models import Inbox, CachedMessage, UserMessage

# Create your views here.
def home(request):
    return render(request, 'message/messages.html')


def user_page(request, username):
    u = User.objects.get(username=username)
    if 'read_messages' in request.POST:
        read_messages = [int(x) for x in request.POST.getlist('read_messages')]
        for m in read_messages:
            UserMessage.objects.filter(id=m).update(read=True)
    if 'delete_messages' in request.POST:
        delete_messages = [int(x) for x in request.POST.getlist('delete_messages')]
        for m in delete_messages:
            UserMessage.objects.get(id=m).delete()
    inbox = None
    try:
        inbox = Inbox.objects.get(owner=u)
    except Inbox.DoesNotExist:
        inbox = Inbox.objects.create(owner=u)
        inbox.save()
    all_messages = inbox.messages.all()
    messages = []
    for m in all_messages:
        try:
            cached_message = CachedMessage.objects.get(id=m.message)
            temp_message = cached_message.message
            brief_message = temp_message[0:40]
            if len(brief_message) < len(temp_message):
                brief_message = brief_message + "..."
            messages.append({'writer': cached_message.writer.username, 'message': brief_message, 'read': m.read, 'exists': True, 'id': m.id})
        except CachedMessage.DoesNotExist:
            messages.append({'exists': False})
    return render(request, 'message/user.html', {'username': username, 'current_user': request.user.username, 'messages': messages})



def view_message(request, username, msg_id):
    id=CachedMessage.objects.get(id=msg_id)
    if request.user.username != username:
        raise Http404
    else:
        message = ''
        brief_message = ''
        writer = ''
        msg_id = int(msg_id)
        try:
            UserMessage.objects.filter(id=msg_id).update(read=True)
            cached_message = CachedMessage.objects.get(id=UserMessage.objects.get(id=msg_id).message)
            writer = cached_message.writer.username
            message = cached_message.message
            brief_message = message[0:40]
            if len(brief_message) < len(message):
                brief_message = brief_message + "..."
        except UserMessage.DoesNotExist:
            pass
        return render(request, 'message/view_message.html', {'username': request.user.username, 'message': {'brief': brief_message, 'message': message, 'writer': writer}})

def send_message(request):
    users=[]
    message=[]
    if 'message' in request.POST:
        message = request.POST['message']
        if len(message) > 1024:
            return render(request, 'message/sendmessage.html', {'username': request.user.username})
        if 'users' in request.POST:
            usernames = request.POST['users'].strip().split(',')
            nonexistent_users = []
            for u in usernames:
                try:
                    users.append(User.objects.get(username=u))
                except User.DoesNotExist:
                    nonexistent_users.append(u)
            con={
            'username': request.user.username,
            'nonexistent_users': nonexistent_users
            }
            render(request, 'message/sendmessage.html', con)
    m = CachedMessage.objects.create(writer=request.user, message=message)
    m.save()
    for u in users:
        if u.is_active:
            inbox = None
            try:
                inbox = Inbox.objects.get(owner=u)
            except Inbox.DoesNotExist:
                inbox = Inbox.objects.create(owner=u)
                inbox.save()
            usermessage = UserMessage(read=False,message=m.id)
            usermessage.save()
            inbox.messages.add(usermessage)
    return render(request, 'message/sendmessage.html', {'username': request.user.username})
