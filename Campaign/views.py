from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Template
from Contact_Grps.models import Grps
from .forms import PostForm,PostForms,CustomEmail,CreateEmail
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import get_object_or_404,reverse
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import ListView, DetailView,UpdateView
from django.contrib.auth.models import User
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.utils.html import strip_tags
from django.utils.module_loading import import_string
from django.conf import settings
import random
import urllib
import requests
# Create your views here.
def campaign(request):
    templates = Template.objects.filter(user = request.user)
    groups = Grps.objects.filter(user=request.user)
    #groups = Grps.objects.get(id=16).contacts.values_list()
    if request.method == "POST":
        gid = request.POST['group']
        password = request.POST['password']
        grp = Grps.objects.get(id=gid).contacts.values_list()
        form = CustomEmail(request.POST)
        if form.is_valid():
            subject= form.cleaned_data['subject']
            for group in grp:
                message = form.cleaned_data['content']
                if message.find(str('%s'))!=-1:
                    message = form.cleaned_data['content'] %(group[2])
                text = strip_tags(message)
                from_email= "'"+str(request.user.email)+"'"
                recipient_list= [group[5]]
                email = request.user.email
                connection = get_connection(
                username=email,
                password=password,
                fail_silently= False,
                )
                msg = EmailMultiAlternatives(subject,text,from_email,recipient_list,connection = connection)
                msg.attach_alternative(message,"text/html")
                print(str(request.user.email).strip())
                msg.send()    
            messages.info(request,'Check Your Email')
            return redirect('campaign')
    else:
        form = CustomEmail()
        return render(request,'Campaign/campaign.html',{'templates':templates,'form':form,'groups':groups})

def usetemplates(request,id):
    templates = Template.objects.filter(user = request.user)
    groups = Grps.objects.filter(user = request.user)
    if request.method == "GET" and id:
        template_instance = Template.objects.get(id=id)
        form = CustomEmail(request.POST or None,initial={'subject':template_instance.subject,'content':template_instance.content})
        return render(request,'Campaign/campaign.html',{'templates':templates,'form':form,'groups':groups})
    elif request.method == "POST":
        gid = request.POST['group']
        password = request.POST['password']
        grp = Grps.objects.get(id=gid).contacts.values_list()
        template_instance = Template.objects.get(id=id)
        form = CustomEmail(request.POST or None,initial={'subject':template_instance.subject,'content':template_instance.content})
        if form.is_valid():
            subject= form.cleaned_data['subject']
            for group in grp:
                message = form.cleaned_data['content']
                if message.find(str('%s'))!=-1:
                    message = form.cleaned_data['content'] %(group[2])
                text = strip_tags(message)
                from_email= "'"+str(request.user.email)+"'"
                recipient_list= [group[5]]
                email = request.user.email
                connection = get_connection(
                username=email,
                password=password,
                fail_silently= False,
                )
                msg = EmailMultiAlternatives(subject,text,from_email,recipient_list,connection = connection)
                msg.attach_alternative(message,"text/html")
                print(str(request.user.email).strip())
                msg.send()    
            messages.info(request,'Check Your Email')
            return redirect('campaign')

class TemplateDetailView(UpdateView):
    model = Template
    form_class = CustomEmail
    template_name = "Campaign/template.html"
    
    success_url = "/"

class CampaignDetailView(DetailView):
    model = Template
    template_name = "Campaign/mycampaign.html"

def postext(request):
    templates = Template.objects.filter(user = request.user)
    if request.method =="POST":
        form = PostForms(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.user = request.user
            text.save()
            return redirect('index')
    else:
        form = PostForms()
    return render(request,'Campaign/text_form.html',{'form': form,'templates':templates})

def get_connection(backend=None, fail_silently=False, **kwds):
    """Load an email backend and return an instance of it.

    If backend is None (default), use settings.EMAIL_BACKEND.

    Both fail_silently and other keyword arguments are used in the
    constructor of the backend.
    """
    klass = import_string(backend or settings.EMAIL_BACKEND)
    return klass(fail_silently=fail_silently, **kwds)

"""def send_mail_to_mul(request):
    if request.method == "POST":
        form = CreateEmail(request.POST)
        if form.is_valid():
            subject='Welcome To Mail Application'
            message = form.cleaned_data['message']
            text = strip_tags(message)
            from_email= request.user.email
            recipient_list=[', ]
            auth_user= form.cleaned_data['email']
            auth_password= form.cleaned_data['password']
            connection = get_connection(
            username=auth_user,
            password=auth_password,
            fail_silently= False,
            )
            msg = EmailMultiAlternatives(subject,text,from_email,recipient_list,connection = connection)
            msg.attach_alternative(message,"text/html")
            msg.send()    
            messages.info(request,'Check Your Email')
            return redirect('sendemail')
    else:
        form = CreateEmail()
        return render(request,'Campaign/sendemail.html',{'form':form})"""
    
