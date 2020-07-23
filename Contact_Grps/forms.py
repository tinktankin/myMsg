from django import forms
from .models import Grps,Contacts
from ckeditor_uploader.widgets import  CKEditorUploadingWidget

class CreateGroupForm(forms.ModelForm):
    gname = forms.CharField(max_length = 50)
    class Meta:
        model= Grps
        fields = ['gname','contacts']
    def __init__(self,*args,**kwargs):
        super(CreateGroupForm,self).__init__(*args,**kwargs)
        self.fields['contacts']= forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset = Contacts.objects.filter(user = self.instance.user))
        self.fields['contacts'].required = True
     
class CreateContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields =  ['name','phone','city','email'] 
    def __init__(self,*args,**kwargs):
        super(CreateContactForm,self).__init__(*args,**kwargs)  
class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name','phone','city','email']


class GroupUpdateForm(forms.ModelForm):
    class Meta:
        model = Grps
        fields = ['gname','contacts']
    
    def __init__(self,*args,**kwargs):
        super(GroupUpdateForm,self).__init__(*args,**kwargs)
        self.fields['contacts']= forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple, queryset = Contacts.objects.filter(user = self.instance.user))
        self.fields['contacts'].required = True