from django.contrib import admin
from django.urls import path, include
from .views import user_authentication, add_new_user, modify_user_information, list_users, delete_user, \
    get_user_emails, user_logout, get_user_information

urlpatterns = [
    path('userauth/', user_authentication, name='user_authentication'),
    path('addusr/', add_new_user, name='add_new_user'),
    path('modusr/', modify_user_information, name='modify_user_information'),
    path('lstusrs/', list_users, name='list_users'),
    path('delusr/', delete_user, name='delete_user'),
    path('loadusremail/', get_user_emails, name='get_user_emails'),
    path('lgout/', user_logout, name='user_logout'),
    path('usrinfo/', get_user_information, name='get_user_information'),
]
