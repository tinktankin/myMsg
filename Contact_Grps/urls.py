from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import createcontacts,contact,group,creategroup,ContactUpdateView,GroupUpdateView
urlpatterns = [
    path('createcontacts/',createcontacts,name="createcontacts"),
    path('allcontacts/',contact,name="allcontacts"),
    path('creategroups/',creategroup,name="creategroup"),
    path('allgroups/',group,name="allgroups"),
    path('contact/(?P<slug>[^/]+)/$/',ContactUpdateView.as_view(),name="editcontacts"),
    path('group/(?P<slug>[^/]+)/$/',GroupUpdateView.as_view(),name="editgroups")
]