from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from TaskApp import views

urlpatterns = [
    url(r'^task/$', views.TaskList.as_view()),
    url(r'^task/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
]
