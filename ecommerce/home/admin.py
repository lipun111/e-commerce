from django.contrib import admin
from .models import Contact, GuestEmail
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('name', 'email')

admin.site.register(Contact,ContactAdmin)
admin.site.register(GuestEmail)
