from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('view_profile/<username>/', views.view_user_profile, name='view_user_profile'),
    path('friend_list/', views.friend_list, name='friend_list'),
    path('connect/<operation>/<username>/',views.change_friend, name='change_friend'),

]
