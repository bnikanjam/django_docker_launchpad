from PIL import Image

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth import get_user_model


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date = models.DateField(auto_now=now)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', default='images/hello_cover.png')

    class Meta:
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    # Set canonical URL for the model
    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Slug URL
        self.slug = slugify(str(self.title))

        # Resize book cover image
        cover_size = (400, 300)
        img = Image.open(self.cover.path)
        img.thumbnail(cover_size)
        img.save(self.cover.path)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='authors')

    def __str__(self):
        return self.review
