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
     
    

