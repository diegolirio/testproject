from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    #url(r'^$', 'core.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),	

	url(r'^core/', include('core.urls', namespace="core")),    
    url(r'^person/', include('person.urls', namespace='person')),
	
    url(r'^admin/', include(admin.site.urls)),
)
