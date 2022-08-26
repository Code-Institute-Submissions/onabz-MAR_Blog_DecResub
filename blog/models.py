from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = ((0, "Draft"), (1, "Published"))

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    body = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=255, unique=True)
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='article_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return '%s - %s' % (self.article.title, self.name)
