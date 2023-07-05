from django.contrib import admin
from .models import CustomUser,person,addr
from django.contrib.auth import get_user_model

admin.site.register(get_user_model())
admin.site.register(person)
admin.site.register(addr)
