from django.contrib import admin

from .models import Voiture, User

# Register your models here.

admin.site.register(Voiture)
admin.site.register(User)