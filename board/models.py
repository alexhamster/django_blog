import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from faker import Faker


class Post(models.Model):
    header = models.CharField(verbose_name='header', help_text='write your header of post', max_length=100, null=True)
    body = models.TextField(verbose_name='text of the post', null=False)
    pub_date = models.DateTimeField(verbose_name='date published', null=False, unique=True, auto_now_add=True)
    # for unique cols index was made!
    views_count = models.IntegerField(verbose_name='views count', default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
               datetime.timedelta(days=7)

    def generate(self, amount=5):
        fake = Faker()
        for i in range(amount):
            # через .create нельзя создавать m2m поля
            Post.objects.create(
                header=fake.name(),
                body=fake.text()
                )


    def __str__(self):
        return self.header


