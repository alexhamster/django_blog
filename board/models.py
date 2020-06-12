import datetime
from django.db import models
from django.utils import timezone


class Post(models.Model):
    header = models.CharField(verbose_name='header', max_length=100, null=True)
    body = models.TextField(verbose_name='text_of_post', null=False, default='Empty post...')
    pub_date = models.DateTimeField(verbose_name='date published')
    views_count = models.IntegerField(verbose_name='views count', default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
               datetime.timedelta(days=7)

    def __str__(self):
        return self.header
