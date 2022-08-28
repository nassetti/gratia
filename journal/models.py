from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
# Create your models here.


STATUS = ((0, "Private"), (1, "Public"))


class Journal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="journal_entry", null=True)
    updated_on = models.DateTimeField(auto_now=True)
    one = models.TextField()
    two = models.TextField()
    three = models.TextField()
    four = models.TextField()
    five = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    title = f"{author}_{created_on}"
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='journal_likes',
        blank=True)
    tags = TaggableManager()

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.author}_{self.created_on}"

    def number_of_likes(self):
        return self.likes.count()

