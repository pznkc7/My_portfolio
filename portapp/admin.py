from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','message','subject')



@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display=('title','organization','description','date_earned')

