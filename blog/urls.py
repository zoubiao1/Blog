from django.conf.urls import url,include
from  views import index as blog_views
urlpatterns = [

    url(r'^index/',blog_views.blog_index,name='blog_index'),


]