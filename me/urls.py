from django.conf.urls import url
from me import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^me/$', views.SnippetList.as_view()),
    url(r'^me/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)