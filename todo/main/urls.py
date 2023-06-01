from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.Todo_main.as_view(), name='main'),
]
