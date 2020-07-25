from django.shortcuts import render,redirect
from .models import Contacts,Grps
from django.contrib import messages
from .forms import CreateGroupForm,ContactUpdateForm,GroupUpdateForm,CreateContactForm
from django.views.generic import UpdateView
from django.utils.text import slugify
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

import csv, io
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
# one parameter named request
def import_csvfiles(request):
    # declaring template
    template = "Contact_Grps/import_csv.html"
    data = Contacts.objects.filter(user = request.user)
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name,phone,city,email', 
        'profiles': data
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        create = Contacts(
            user= request.user,
            name=column[0],
            phone=column[1],
            city=column[2],
            email=column[3],
        )
        create.save()
        # print(3)
        conid = create.id
        contact = Contacts.objects.get(id=conid)
        contact.slug = slugify(contact.name)+'_'+str(conid)
        #contact.save()
    return redirect('import')
        
    context = {}
    return render(request, template, context)