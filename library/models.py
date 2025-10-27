from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    cover = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-created_at']


def __str__(self):
    return f"{self.title} — {self.author}"


def get_absolute_url(self):
    return reverse('library:book-detail', args=[str(self.pk)])