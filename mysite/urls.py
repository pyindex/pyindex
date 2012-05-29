from django.conf.urls.defaults import *
import os
#-*- coding: utf-8 -*-

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': os.path.join(os.path.dirname(__file__),'/media').replace("\\","/")}),
)

urlpatterns += patterns('mysite.pydef.views',
    (r'^$', 'intro'),                
    (r'^index/$', 'index'),                          ## 
	(r'^search//$', 'index'),                        ## 
	(r'^search/index/(?P<input>[A-Z_#])/$', 'searchindex'),   ##
	(r'^search/(?P<input>[\w]{1,50})/$', 'searchname'),  ## 
	(r'^edit/$', 'edit_this_part'),  ## 
)

urlpatterns += patterns('mysite.pydef.views',
    (r'', 'error'),
)

urlpatterns += patterns('',
    #(r'', 'index'),
)
