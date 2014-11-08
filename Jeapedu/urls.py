from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()
import settings
import xadmin

xadmin.autodiscover()

from xadmin.plugins import xversion
#xversion.registe_models()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Jeapedu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'xadmin/', include(xadmin.site.urls)),
	
	#url(r'^course/$', 'Jeapedu.views.course', name='course'),
	url(r'^courseshow/(\d+)/$', 'Jeapedu.views.courseshow', name='courseshow'),
	url(r'^teachers$', 'Jeapedu.views.teachers', name='teachers'),
	url(r'^$', 'Jeapedu.views.index', name='index'),
	url(r'^course/page=(\d+)/$','Jeapedu.views.paginator',name='paginator'),
    url(r'^teachers/page=(\d+)/$','Jeapedu.views.paginator_teachers',name='paginator_teachers'),

    url(r'^media(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT,'show_indexes':True}),
	
)
