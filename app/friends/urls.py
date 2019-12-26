from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^populateData$', views.populateData, name='populateData'),
    url(r'^getUsers$', views.getUsers, name='getUsers'),
    url(r'^getFriends$', views.getFriends, name='getFriends'),
    url(r'^getFriendsRecommendation$', views.getFriendsRecommendation, name='getFriendsRecommendation'),
]
