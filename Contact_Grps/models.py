from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.text import slugify
# Create your models here.
class Contacts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 12,)
    city = models.CharField(max_length = 100)
    email = models.EmailField()
    slug = models.SlugField(unique=True, allow_unicode=True)
    
    def save(self,*args,**kwargs):
        super(Contacts, self).save(*args, **kwargs)
        self.slug = slugify(self.name)+'_'+str(self.id)
        return super(Contacts,self).save(*args,**kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("editcontacts", kwargs={
            'slug': self.slug
        })

    
class Grps(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gname = models.CharField(max_length = 100)
    contacts = models.ManyToManyField(Contacts)
    slug = models.SlugField(unique=True, allow_unicode=True)

    def save(self,*args,**kwargs):
        super(Grps, self).save(*args, **kwargs)
        self.slug = str(self.id)
        return super(Grps,self).save(*args,**kwargs)

    def __str__(self):
        return self.gname
        
    def get_absolute_url(self):
        return reverse("editgroups", kwargs={
            'slug': self.slug
        })