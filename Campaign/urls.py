from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .views import campaign,usetemplates,TemplateDetailView,postext,CampaignDetailView
urlpatterns = [
    path('campaign/',campaign,name="campaign"),
    path('campaign/<int:id>',usetemplates,name ="templates"),
    path('update/(?P<slug>[^/]+)/$',TemplateDetailView.as_view(),name="stored"),
    path('context/',postext,name="context"),
    path('campaign/(?P<slug>[^/]+)/$/', CampaignDetailView.as_view(), name='webpages'),

]
