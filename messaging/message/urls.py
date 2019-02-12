from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='message'),
    path('<username>/inbox/', views.user_page, name='user_page'),
    path('sendmessage/', views.send_message, name='send_message'),
    path('<username>/<msg_id>/', views.view_message, name='view_message'),

]
