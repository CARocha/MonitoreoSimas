from django.conf.urls.defaults import *
from monitoreo.settings import *
from os import path as os_path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin_tools/', include('admin_tools.urls')),
    # Example:
    # (r'^Monitoreo/', include('Monitoreo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'monitoreo.simas.views.index'),
    (r'^', include('monitoreo.simas.urls')),
)

if DEBUG:
    urlpatterns += patterns('',
                            (r'^archivos/(.*)$', 'django.views.static.serve',
                             {'document_root': os_path.join(MEDIA_ROOT)}),
                           )
