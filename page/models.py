from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class Page(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Draft'
        PUBLISHED = 'published', 'Published'
        ARCHIVED = 'archived', 'Archived'
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    content = RichTextField()  
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posts = models.ManyToManyField('Post', related_name='pages', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['order', 'created_at']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'


class Config(models.Model):
    site_name = models.CharField(max_length=255)
    site_description = models.TextField()
    site_keywords = models.CharField(max_length=255)
    site_logo = models.ImageField(upload_to='logos/')
    site_favicon = models.ImageField(upload_to='favicons/')
    config_json = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    tags = models.ManyToManyField('Tags', related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Tags(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'



class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption if self.caption else 'Image'


class HomePage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    posts = models.ManyToManyField(Post, related_name='home_pages', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home_page_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Pages'

