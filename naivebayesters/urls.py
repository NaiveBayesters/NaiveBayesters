from django.conf.urls import include, url
from django.contrib import admin
from classifier import views

urlpatterns = [
    url(r'^', include('classifier.urls')),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', views.register, name='register'),
    url(r'^user_redirect/', views.user_redirect, name='user_redirect'),
]
