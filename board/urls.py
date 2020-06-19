from django.urls import path
from board.views import BoardView, PostView
from .views import CreatePost

app_name = 'board'

urlpatterns = [
    path('', BoardView.as_view(), name='board'),
    path('<int:pk>/', PostView.as_view(), name='post-detail'),
    path('create/', CreatePost.as_view(), name='board_post'),
]