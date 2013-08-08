from django.conf.urls import patterns, include, url
from dzuno import views as dz
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import os
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$',dz.home),
	url(r'^ajax/(?P<seccion>\w{1,8})/$',dz.get_ajax_data),


    # Examples:
    # url(r'^$', 'henocdz.views.home', name='home'),
    # url(r'^henocdz/', include('henocdz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^adpy/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^adpy/', include(admin.site.urls)),

    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')}),
)
