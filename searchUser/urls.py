from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tweet_list, name = 'searchuser'),
    url(r'^get_queryset/$',views.get_queryset)
]