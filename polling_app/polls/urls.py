from . import views
from django.conf.urls import url

urlpatterns = [
    #index page
    #ex: /polls/
    url(r'^$', views.IndexView.as_view(), name='index'),

    #detail page
    #ex: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    #results page
    #ex: /polls/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),

    #voting page
    #ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
