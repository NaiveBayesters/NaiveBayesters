from django.conf.urls import url, include

from . import views

app_name = "classifier"

urlpatterns = [
    url(r'^home/', views.home, name="home_page"),
    url(r'^profile/', views.profile, name="profile_page"),
    url(r'^train/', views.train, name="training_page"),
    url(r'^classifier/(?P<id>[0-9]+)/', views.classifier_detail_view, name="classifier_detail"),
     # Auth-related URLs:
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^loggedin/$', 'classifier.views.loggedin', name='loggedin'),
    # Registration URLs
    url(r'^register/$', 'classifier.views.register', name='register'),
    url(r'^register/complete/$', 'classifier.views.registration_complete', name='registration_complete'),
    ]
