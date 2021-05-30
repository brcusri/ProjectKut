import uuid

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    Status = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=Status)

    slug = models.SlugField(unique=True,null=False)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    craeted_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '->'.join(full_path[::-1])
    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug':self.slug})

class Book(models.Model):
    Status = (
        ('True','Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    Image = models.ImageField(blank=True, upload_to='images/')
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    edition = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    detail = RichTextUploadingField()
    slug = models.SlugField(unique=True, default=uuid.uuid1)
    status = models.CharField(max_length=10, choices=Status)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height=50 />'.format(self.Image.url))
    image_tag.short_description='Image'
    def get_absolute_url(self):
        return reverse('books_detail', kwargs={'slug':self.slug})

class Images(models.Model):

    books = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height=50 />'.format(self.image.url))
    image_tag.short_description='Image'

class Comment(models.Model):
    Status = (
        ('New', 'New'),
        ('True', 'Yes'),
        ('False','No'),
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField( max_length=150, blank= True)
    comment = models.TextField(blank=True)
    rate = models.IntegerField(blank=True)
    Status = models.CharField(max_length=10,choices=Status, default='New')
    ip = models.CharField(blank=True, max_length=20)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return self.subject


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']





