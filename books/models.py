from django.db import models

class Category(models.Model):
    Status = (
        ('True','Evet'),
        ('False','Hayır'),
    )
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=Status)

    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    craeted_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=Status)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.title

