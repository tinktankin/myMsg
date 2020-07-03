from django import forms
from .models import Template
from ckeditor_uploader.widgets import  CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
class PostForms(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Template
        fields = ['subject','content']

class CreateEmail(forms.Form):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    email  = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class CustomEmail(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Template
        fields = ['subject','content']
    def __init__(self,*args,**kwargs):
        super(CustomEmail,self).__init__(*args,**kwargs)