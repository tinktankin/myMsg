from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Contacts,Grps
from .forms import CreateGroupForm
# Register your models here.
admin.site.register(Contacts)
class MyModelAdmin(admin.ModelAdmin):
    form = CreateGroupForm
admin.site.register(Grps,MyModelAdmin)
# Register your models here.
