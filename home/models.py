from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea


class Settings(models.Model):
    Status = (
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    keywords = models.CharField(max_length=150)
    company = models.CharField(max_length=50)
    adress = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=20)
    smtpemail = models.CharField(blank=True,max_length=20)
    smtppassword = models.CharField(blank=True,max_length=10)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutUs = RichTextUploadingField(blank=True)
    contact = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=Status)

    craeted_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContactFormMessage(models.Model):
    Status =(
        ('New','New'),
        ('Read','Read'),
        ('Closed','Closed'),
    )
    name =models.CharField(max_length=20,blank=True)
    email = models.CharField(max_length=50,blank=True)
    subject = models.CharField(max_length=50,blank=True)
    message = models.CharField(max_length=255,blank=True)
    Status = models.CharField(max_length=10,choices=Status,default='New')
    ip = models.CharField(max_length=20,blank=True)
    note = models.CharField(max_length=100, blank=True)

    craeted_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'email': TextInput(attrs={'class': 'input', 'placeholder': 'E-Mail'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder':'Subject'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Message', 'rows': '5'})
        }