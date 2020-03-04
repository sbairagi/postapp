from django.contrib import admin
from .models import Blogpost,Userdetails
# Register your models here.
admin.site.register(Userdetails)
admin.site.register(Blogpost)