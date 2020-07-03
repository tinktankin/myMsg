from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import signup,LoginView,logout,index,activate_account
urlpatterns = [
    path('signup/',signup,name="signup"),
    path('signin/',LoginView.as_view(),name="signin"),
    path('activate/<slug:uidb64>/<slug:token>/',activate_account, name='activate'),
    path('logout/',logout,name="logout"),
    path('',index,name="index"),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='user/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='user/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='user/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='user/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    

]