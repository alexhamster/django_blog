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


class PostView(DetailView):
    template_name = 'board/post.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CreatePost(CreateView):
    model = Post
    success_url = '/board/'
    fields = ['header', 'body']