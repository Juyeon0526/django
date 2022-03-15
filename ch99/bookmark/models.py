from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField('Title', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        db_table = 'bookmark_urls'
        ordering = ('-modify_dt',)

    def get_absolute_url(self):
        return reverse('bookmark:detail', kwargs={'pk':self.id})
