from django.conf.urls import url

from . import views

# Examples:
# ex: /polls/
# ex: /polls/5/
# ex: /polls/5/results/
# ex: /polls/5/vote/

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
