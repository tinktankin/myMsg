from django.shortcuts import render,redirect
from .models import Social
from .forms import Social_form
from Campaign.models import Template
from django.contrib.sites.models import Site

# Create your views here.

def social(request):
    if request.method == "POST":
        form = Social_form(request.POST)
        if form.is_valid():
            social = form.save(commit=False)
            social.user = request.user
            social.save()
            return redirect('Social')
    else:
        
        if Social.objects.filter(user=request.user).exists():
            social = Social.objects.get(user=request.user)
            templates = Template.objects.filter(user=request.user)
            return render(request,'Social/social_share.html',{'templates':templates,'social':social})
        else:
            form = Social_form()
            return render(request,'Social/share_form.html',{'form':form})


def share(request,id):
    social = Social.objects.get(user=request.user)
    templates = Template.objects.filter(user=request.user)
    temp = Template.objects.get(id =id)
    url = temp.get_absolute_url
    
    return render(request,'Social/social_share.html',{'templates':templates,'social':social,'url':url})



