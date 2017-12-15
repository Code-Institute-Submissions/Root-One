from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from hello import views as hello_views
from accounts import views as accounts_views
from paypal_store import views as paypal_views
from products import views as product_views
from paypal.standard.ipn import urls as paypal_urls
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # URL for launch page
    url(r'^pages', hello_views.get_index, name='index'),

    # URLs for flatpages
    url(r'^pages', include('django.contrib.flatpages.urls')),

    #URL for about me page
    url(r'^about', hello_views.get_about, name='about'),

    # URLs for recipes blog
    url(r'^blog/', include('recipes_blog.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # URLs for accounts
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    # URLs for paypal purchases
    url(r'^a-specific-url-for-payments/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),

    #URL for our products
    url(r'^products/$', product_views.all_products),
    url(r'^products/(?P<id>\d+)/$', product_views.product_detail),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns.append(url(r'^debug/', include(debug_toolbar.urls)))