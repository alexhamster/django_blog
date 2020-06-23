from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from board.models import Post
from django.views.generic.list import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
# Create your views here.

class IndexView(TemplateView):
    template_name = 'board/index.html'


class BoardView(ListView):
    model = Post
    template_name = 'board/board.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class PostView(TemplateView):
    template_name = 'board/post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.prefetch_related('rubrics').get(id=self.kwargs['pk'])  # get return ONE object: Post
        # in case of MANY objects it throws exception
        context['rubrics'] = list(post.rubrics.all())
        context['comments'] = list(post.comment_set.all())
        context['post'] = post
        return context


class CreatePost(CreateView):
    model = Post
    success_url = '/board/'
    fields = ['header', 'body']

