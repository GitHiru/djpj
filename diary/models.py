from django.db import models
from django.utils import timezone


class Category(models.Model):
    name      = models.CharField(max_length=255)
    slug      = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name      = models.CharField(max_length=255)
    slug      = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    category     = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags         = models.ManyToManyField(Tag, blank=True)
    title        = models.CharField(max_length=255)
    description  = models.TextField(blank=True)
    content      = models.TextField()
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public    = models.BooleanField(default=False)
    image        = models.ImageField(upload_to='post_images/', null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'pk:{self.pk} title:{self.title} created_at:{self.created_at}'


class ContentImage(models.Model):
    post          = models.ForeignKey(Post, on_delete=models.PROTECT)
    content_image = models.ImageField(upload_to='post_content_images/')
