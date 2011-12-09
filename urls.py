from django.conf.urls.defaults import patterns, include, url
from piston.resource import Resource

from irocservices.handlers import CoriHandler, CoriCountHandler

cori_resources = Resource(handler=CoriHandler)
cori_count_resources = Resource(handler=CoriCountHandler)

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('irocservices.cori.urls'), name='api_home'),

    # Get Comments
    url(r'^apis/(?P<id_table>[^/]+)/(?P<id_news>[^/]+)/$', cori_resources, { 'emitter_format': 'xml' }),
    url(r'^apis/(?P<id_table>[^/]+)/(?P<id_news>[^/]+)/(?P<emitter_format>.+)$', cori_resources),

    # Count Comments
    url(r'^capis/(?P<id_table>[^/]+)/(?P<id_news>[^/]+)/$', cori_count_resources, { 'emitter_format': 'xml' }),
    url(r'^capis/(?P<id_table>[^/]+)/(?P<id_news>[^/]+)/(?P<emitter_format>.+)$', cori_count_resources),
)
