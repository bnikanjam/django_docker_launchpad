from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.text import slugify


class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        abstract = True
        ordering = ['-updated_at']


class Post(BaseModel):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=127, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta(BaseModel.Meta):
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f'{self.author} -> {self.title[:64]}'

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.slug])


class Review(BaseModel):
    author = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    review = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta(BaseModel.Meta):
        ordering = ['-updated_at']
        verbose_name = 'review'
        verbose_name_plural = 'reviews'

    def __str__(self):
        return f'Review by:  {self.author}  for:    {self.content[:64]}'
