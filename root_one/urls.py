from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from hello import views as hello_views
from accounts import views as accounts_views
from threads import views as forum_views
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # URLs for launch page
    url(r'^$', hello_views.get_index, name='index'),

    # URLs for flatpages
    url(r'^pages/', include('django.contrib.flatpages.urls')),

    # URLs for recipes blog
    url(r'^blog/', include('recipes_blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # URLs for accounts
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # URLs for Forum
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$',  forum_views.new_thread, name='new_thread'),

    # URL for tinymce
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))