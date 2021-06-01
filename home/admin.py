from django.contrib import admin
from home.models import Settings, ContactFormMessage, UserProfile, faq

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','Status','note']
    list_filter = ['Status']

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','phone','city','country','image_tag',]
    list_filter = ['country','city']

class faqAdmin(admin.ModelAdmin):
    list_display = ['question','answer','Status']
    list_filter = ['Status']


admin.site.register(ContactFormMessage,ContactFormAdmin)
admin.site.register(Settings)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(faq,faqAdmin)
