from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView,UpdateView
from django.views.generic.edit import CreateView 
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.utils.html import strip_tags
from django.utils.module_loading import import_string
from django.conf import settings
import random
import urllib
import requests
from django.shortcuts import get_object_or_404,reverse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def index(request):
    return render(request,'user/home.html')

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')
def signup(request):
    if request.method =="POST":
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email Exists')
                return redirect('signup')
            elif User.objects.filter(username=user_name).exists():
                messages.error(request, "UserName has been Taken. Try New One.")
                return redirect('signup')
            else:
                user = User.objects.create_user(username = user_name,email= email, password = password1 ,is_active =False )
                user.save()
                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('user/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                })
                to_email = email
                email = EmailMessage(email_subject, message, to=[to_email])
                email.send()
                return HttpResponse('We have sent you an email, please confirm your email address to complete registration')
        else:
            messages.info(request,'Wrong Password')
            return redirect('signup')
    else:
        return render(request,'user/index.html')
def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user

    return None

class LoginView(View):
    template_name = 'user/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate_user(email, password)

        if user is not None:
            if user.is_active:
                auth.login(request, user,backend='django.contrib.auth.backends.ModelBackend')

                return redirect('index')
            else:
                messages.info(request,'User not active')
        else:
            messages.info(request,'Invalid Credentials')

        return render(request, self.template_name)

def logout(request):
    auth.logout(request)
    return redirect('index')

def team(request):
    return render(request,'user/team.html')








