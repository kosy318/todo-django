from . import views
from django.conf.urls import url

app_name = 'board'

urlpatterns = [
    url(r'^$', views.Todo_board.as_view(), name='board'),
    url(r'^insert/$', views.check_post, name='board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Board_detail.as_view(), name='board_detail'),
]
