from django.shortcuts import render,redirect
from .models import Contacts,Grps
from django.contrib import messages
from .forms import CreateGroupForm

# Create your views here.
def contact(request):
    contacts = Contacts.objects.filter(user = request.user)
    groups = Grps.objects.filter(user = request.user)
    return render(request,'Contact_Grps/contacts.html',{'contacts':contacts,'groups':groups})

def group(request):
    groups = Grps.objects.filter(user = request.user)
    return render(request,'Contact_Grps/groups.html',{'groups':groups})

def createcontact(request):
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        city = request.POST['city']
        if Contacts.objects.filter(email = email).exists():
                messages.info(request,'This contact is already added.')
                return redirect('createcontact')
        else:
            contact = Contacts.objects.create(user = request.user, name = name,email= email, phone = phone , city = city)
            contact.save()
            messages.info(request,'Contact Added Successfully.')
            return redirect('allcontacts')
    else:
        return render(request,'Contact_Grps/createcon.html')

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