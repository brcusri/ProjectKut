from django.contrib import admin
from home.models import Settings, ContactFormMessage

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','Status','note']
    list_filter = ['Status']

admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Settings)
