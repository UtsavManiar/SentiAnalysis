from django.conf.urls import url
from . import views

urlpatterns  = [
    url(r'^$',views.home,name='home'),
    #url(r'^about.html$',views.about,name='about'),
    url(r'^user$',views.offline,name='offline'),
    url(r'^dynamic$',views.index,name='index'),
	url(r'^tweetling/online$',views.index,name='index'),
	url(r'^tweetling/$',views.home,name='home'),
	url(r'^tweetling/user$',views.offline,name='offline'),
	url(r'^tweetling/dynamic$',views.index,name='index'),
]


