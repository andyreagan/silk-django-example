from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView,RedirectView

from django.contrib import admin
admin.autodiscover()
  
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/',
        TemplateView.as_view(template_name='testsite/index.html'),
        name='index'),
)
