from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<url>\w+)/$', views.index, name='index'),
]