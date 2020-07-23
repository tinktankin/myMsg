from django.shortcuts import render,redirect
from .models import Contacts,Grps
from django.contrib import messages
from .forms import CreateGroupForm,ContactUpdateForm,GroupUpdateForm,CreateContactForm
from django.views.generic import UpdateView
# Create your views here.
def contact(request):
    contacts = Contacts.objects.filter(user = request.user)
    groups = Grps.objects.filter(user = request.user)
    return render(request,'Contact_Grps/contacts.html',{'contacts':contacts,'groups':groups})

def group(request):
    groups = Grps.objects.filter(user = request.user)
    return render(request,'Contact_Grps/groups.html',{'groups':groups})

def createcontacts(request):
    if request.method =="POST":
        form = CreateContactForm(request.POST)
        if Contacts.objects.filter(email = form['email'] ,user=request.user).exists():
                messages.info(request,'This contact is already added.')
                return redirect('createcontacts')
        if form.is_valid():
            cons = form.save(commit=False)
            cons.user = request.user
            cons.save()
            return redirect('allcontacts')
    else:
        form = CreateContactForm()
        return render(request,'Contact_Grps/createcon.html',{'form':form})

def creategroup(request):
    if request.method =="POST":
        form = CreateGroupForm(request.POST,instance=Grps(user=request.user))
        if form.is_valid():
            grps = form.save(commit=False)  
            grps.user = request.user
            grps.save()
            form.save_m2m()
            messages.info(request,'Group added successfully')
            return redirect('allgroups')
    else:
        form = CreateGroupForm(instance=Grps(user=request.user))
    return render(request,'Contact_Grps/grps_form.html',{'form': form})

class ContactUpdateView(UpdateView):
    model = Contacts
    form_class = ContactUpdateForm
    template_name = "Contact_Grps/updatecontact.html"
    
    success_url = "/"

class GroupUpdateView(UpdateView):
    model = Grps
    form_class = GroupUpdateForm
    template_name = "Contact_Grps/updategroup.html"
    
    success_url = "/"