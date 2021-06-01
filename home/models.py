from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import  RichTextUploadingField
# Create your models here.
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone =models.CharField(blank=True, max_length=20)
    adress = models.CharField(blank=True, max_length=200)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=20)
    image = models.ImageField(blank=True, upload_to='images/user/',default='images/user/user.jpg')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '[' + self.user.username + ']' + ' ' + self.user.email

    def image_tag(self):
        return mark_safe('<img src="{}" height=50 />'.format(self.image.url))
    image_tag.short_description = 'Image'


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone', 'adress', 'city', 'country', 'image')


class faq(models.Model):
    Status = (('True','True'),
              ('False', 'False'))
    question = models.CharField(max_length=150)
    answer = models.CharField(max_length=150)
    keywords = models.CharField(max_length=20)
    Status = models.CharField(max_length=10, choices=Status)

    craeted_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question