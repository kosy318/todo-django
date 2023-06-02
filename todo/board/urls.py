from . import views
from django.conf.urls import url

app_name = 'board'

urlpatterns = [
    url(r'^$', views.Todo_board.as_view(), name='board'),
    url(r'^insert/$', views.check_post, name='board_insert'),
    url(r'^(?P<pk>[0-9]+)/detail/$', views.Board_detail.as_view(), name='board_detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.Board_update.as_view(), name='board_update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.Board_delete.as_view(), name='board_delete'),
    url(r'^update_complete/$', views.update_complete, name='update_complete'),
]
