import datetime
from django.db import models
from django.utils import timezone
from faker import Faker
import random
from django.contrib.auth.models import User

class Rubric(models.Model):
    name = models.CharField(verbose_name='rubric', max_length=100, null=False, unique=True)
    description = models.CharField(verbose_name='rubric description', max_length=300, blank=True)

    class Meta:
        verbose_name = 'Rubric'
        verbose_name_plural = 'Rubrics'
        ordering = ['name']

    def generate(self):
        names = ['C++', 'Python', 'Hobby', 'Lifestyle', 'Sport', 'Games', 'Web', 'SQL']
        fake = Faker()
        for i in names:
            Rubric.objects.create(
                name=i,
                description=fake.text()
            )

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(verbose_name='comment', max_length=300)
    pub_date = models.DateTimeField(verbose_name='time commented', auto_now_add=True)
    rating = models.SmallIntegerField(verbose_name='rating', default=0, editable=False)
    to_post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='comment for a post')
    answer_to_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE)  # an answer to another comment
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='author of comment', null=True)
    sender_email = models.EmailField(verbose_name='email of sender', default='anon@ya.ru', null=False)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'

    def __str__(self):
        return self.text


class Post(models.Model):
    header = models.CharField(verbose_name='header', help_text='write your header of post', max_length=100, null=True)
    body = models.TextField(verbose_name='text of the post', null=False)
    pub_date = models.DateTimeField(verbose_name='date published', null=False, unique=True, auto_now_add=True)
    views_count = models.IntegerField(verbose_name='views count', default=0)
    rubrics = models.ManyToManyField(Rubric, through='Kit', through_fields=('post', 'rubric'))

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['pub_date', 'views_count']

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - \
               datetime.timedelta(days=7)

    def generate_rubrics(self, amount=10):
        fake = Faker()
        for i in range(amount):
            # через .create нельзя создавать m2m поля, надо чтобы оба инстенса были в бд
            all_rubrics = list(Rubric.objects.all())
            instance = Post.objects.create(
                header=fake.name(),
                body=fake.text(),
            )
            instance.rubrics.add(*random.sample(all_rubrics, random.randint(1, len(all_rubrics))))

    def generate_comments(self, amount=5):  # generate random count of comments for every post
        faker = Faker()
        for post in Post.objects.all():
            for i in range(amount):
                instance = Comment.objects.create(
                    text=faker.text(),
                    to_post=post,
                    sender_email=faker.name().replace(' ', '_') + '@ya.ru',
                )


    def __str__(self):
        return self.header


class Kit(models.Model):
    post = models.ForeignKey(Post, on_delete=models.DO_NOTHING)
    rubric = models.ForeignKey(Rubric, on_delete=models.DO_NOTHING)
    rubric_priority = models.IntegerField(default=0)

'''
from board.models import *
p = Post()
p.generate_comments()
'''
