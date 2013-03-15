from django.conf.urls import patterns, include, url
from django.contrib import admin

from settings import MEDIA_ROOT

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sugu.views.home', name='home'),
    # url(r'^sugu/', include('sugu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    url(r'^media/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': MEDIA_ROOT, 'show_indexes': True},
         name='media'),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
)
