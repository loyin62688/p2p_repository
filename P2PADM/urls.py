from django.conf.urls import patterns, include, url
from django.contrib import admin
from P2PADM.apps.P2Padmin.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'P2PADM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',login),
    url(r'^login/$',login),
    url(r'^p2pinfo/(.*)$',requires_login(p2pInfoMon)),
    url(r'^downloadcsv',requires_login(downloadP2PCSV)),
)
