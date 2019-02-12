from django.urls import path
from . import views

urlpatterns = [
    path('bio/', views.bio, name='bio'),
    path('bio/edit/', views.edit_bio, name='edit_bio'),
    path('bio/change_password/', views.change_password, name='change_password'),
    path('', views.index, name='index'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]
