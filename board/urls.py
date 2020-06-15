from django.urls import path
from board.views import IndexView
from .views import CreatePost

app_name = 'board'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', CreatePost.as_view(), name='board_post'),
]