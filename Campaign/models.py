from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from ckeditor_uploader.fields import  RichTextUploadingField
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.
class ModelClass:
    ## content = models.TextField()
    content = RichTextUploadingField()

class Template(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)  
    content = RichTextUploadingField()
    slug = models.SlugField(unique=True, allow_unicode=True)
    
    def save(self,*args,**kwargs):
        super(Template, self).save(*args, **kwargs)
        self.slug = slugify(self.subject)+ "-" + str(self.id)
        return super(Template,self).save(*args,**kwargs)
    def __str__(self):
        return self.subject
    
    def get_absolute_urls(self):
        return reverse("stored", kwargs={
            'slug': self.slug
        })

    def get_absolute_url(self):
        return reverse("webpages", kwargs={
            'slug': self.slug
        })


class Campaign(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    camp_name = models.CharField(max_length=200,blank=True)
    sent_to = models.CharField(max_length=1000,blank=True)
    no_of_receivers = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True)

