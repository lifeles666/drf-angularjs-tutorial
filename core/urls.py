from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from news.views import Homepage

urlpatterns = patterns('',
    url(
        regex = r'^$', 
        view = Homepage.as_view(),
        name = 'home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^news', include('news.urls')),
)
