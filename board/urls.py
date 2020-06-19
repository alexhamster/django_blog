from django.urls import path
from board.views import BoardView
from .views import CreatePost

app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('create/', CreatePost.as_view(), name='board_post'),
]