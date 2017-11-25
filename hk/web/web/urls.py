from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'aqp.views.home', name='home'),
    url(r'^about', 'aqp.views.about', name='about'),
    url(r'^contact', 'aqp.views.contact', name='contact'),



    # url(r'^blog/', include('blog.urls')),
    #(?P<all_items>.*)
    #(?P<id>\d+)
    url(r'^admin/', include(admin.site.urls)),

)


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
