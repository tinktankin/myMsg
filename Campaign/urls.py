from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from .views import campaign,usetemplates,TemplateDetailView,postext,CampaignDetailView,image_load,manual_contact_campaign,usetemplates_mancontacts_camp,sentbox
urlpatterns = [
    path('campaign/',campaign,name="campaign"),
    path('campaign0/',manual_contact_campaign,name="manual_campaign"),
    path('campaign0/<int:id>',usetemplates_mancontacts_camp,name ="manual_templates"),
    path('campaign/<int:id>',usetemplates,name ="templates"),
    path('update/(?P<slug>[^/]+)/$',TemplateDetailView.as_view(),name="stored"),
    path('context/',postext,name="context"),
    path('campaign/(?P<slug>[^/]+)/$/', CampaignDetailView.as_view(), name='webpages'),
    path('image_load/<int:id>', image_load, name='image_load'),
    path('sentbox/',sentbox,name='sentbox'),
]
