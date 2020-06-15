from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from board.models import Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'board/index.html'


class CreatePost(CreateView):
    model = Post
    success_url = '/board/'
    fields = ['header', 'body']