from django.conf.urls import url
from recipes_blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.post_lists),
    url(r'^(?P<id>\d+)/$', blog_views.post_detail),
]
