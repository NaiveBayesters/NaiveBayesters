from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="home"),
    url(r'^profile/(?P<pk>[0-9]+)', views.profile, name="profile"),
]
