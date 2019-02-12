from django.contrib import admin
from .models import CachedMessage,Inbox,UserMessage

# Register your models here.
admin.site.register(Inbox)

admin.site.register(CachedMessage)
admin.site.register(UserMessage)
