from django.urls import path
from board.views import IndexView
app_name = 'board'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]