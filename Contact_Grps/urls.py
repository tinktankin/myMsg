from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import createcontact,contact,group,creategroup
urlpatterns = [
    path('createcontacts/',createcontact,name="createcontacts"),
    path('allcontacts/',contact,name="allcontacts"),
    path('creategroups/',creategroup,name="creategroup"),
    path('allgroups/',group,name="allgroups"),
]