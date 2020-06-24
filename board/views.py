from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, FormView
from board.models import Post, Comment
from django.views.generic.list import ListView
from django.utils import timezone
from django.forms import ModelForm
from django import forms
# Create your views here.


class IndexView(TemplateView):
    template_name = 'board/index.html'


class UserView(TemplateView):
    template_name = 'board/cabinet.html'


class BoardView(ListView):
    model = Post
    template_name = 'board/board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('sender_email', 'text')


class PostView(FormView):
    template_name = 'board/post.html'
    form_class = CommentForm
    success_url = '/board/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.prefetch_related('rubrics').get(id=self.kwargs['pk'])  # get return ONE object: Post
        # in case of MANY objects it throws exception
        context['rubrics'] = list(post.rubrics.all())
        context['comments'] = list(post.comment_set.all())
        context['post'] = post

        #print(context)
        # in template name 'form' used as default
        return context

    def form_valid(self, form):  # вызывается когда валидная форма POSTed
        model_instance = form.save(commit=False)  # return model instance without saving to db
        model_instance.to_post = Post.objects.get(id=self.kwargs['pk'])  # TODO refactor?
        if self.request.user.is_authenticated:  # using for auth users theirs emails
            model_instance.sender_email = self.request.user.email
        form.save()
        return super().form_valid(form)


class CreatePost(CreateView):
    model = Post
    success_url = '/board/'
    fields = ['header', 'body']


