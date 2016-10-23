"""Urls for the demo of Silent Auction"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include

from django.views.static import serve
from django.views.defaults import bad_request
from django.views.defaults import server_error
from django.views.defaults import page_not_found
from django.views.defaults import permission_denied
from django.views.generic.base import RedirectView

from rest_framework.authtoken import views


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/silent-auction/', permanent=True)),
    url(r'^silent-auction/', include('silent_auction.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', views.obtain_auth_token),
]

urlpatterns += [
    url(r'^400/$', bad_request),
    url(r'^403/$', permission_denied),
    url(r'^404/$', page_not_found),
    url(r'^500/$', server_error),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT})
    ]