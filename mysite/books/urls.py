from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^META/$', views.display_meta, name='meta'),
    url(r'^search/$', views.search, name='search'),
]
