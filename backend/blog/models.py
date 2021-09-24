from django.db import models
from django.conf import settings

from tinymce.models import HTMLField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True),
    bio = models.CharField(max_length=240,blank=True)

    def __str__(self):
        return self.user.get_username()

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    post_image = models.URLField(max_length = 500 ,default='https://cdn.pixabay.com/photo/2018/04/06/13/46/poly-3295856_960_720.png')
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    truncated_body = HTMLField(default='Article Intro')
    body = HTMLField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    popular = models.BooleanField(default=False)
    reading_time = models.CharField(max_length=150, blank=True)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)


class Email(models.Model):
    email = models.EmailField(max_length=200, unique=True)

    def __str__(self):
        return self.email


class Message(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    message = models.TextField(max_length=50000)
    read = models.BooleanField(default=False)