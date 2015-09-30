from . import views
from django.conf.urls import url

urlpatterns = [
    #index page
    #ex: /polls/
    url(r'^$', views.index, name='index'),

    #detail page
    #ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

    #results page
    #ex: /polls/5/results
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    #voting page
    #ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
