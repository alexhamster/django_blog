import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save


class Post(models.Model):
    header = models.CharField(verbose_name='header', max_length=100, null=True)
    body = models.TextField(verbose_name='text_of_post', null=False, default='Empty post...')
    pub_date = models.DateTimeField(verbose_name='date published', null=False)
    views_count = models.IntegerField(verbose_name='views count', default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
               datetime.timedelta(days=7)

    def __str__(self):
        return self.header


def fill_current_date(sender, instance: Post, **kwargs):
    instance.pub_date = timezone.now()


pre_save.connect(fill_current_date, sender=Post)
