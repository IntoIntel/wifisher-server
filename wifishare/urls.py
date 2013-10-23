from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'point_store.views.index', name='index'),
    url(r'^push$', 'point_store.views.push', name='push'),
    url(r'^points$', 'point_store.views.points', name='points'),
    url(r'^point$', 'point_store.views.point', name='point'),
    url(r'^heatmap$', 'point_store.views.heat', name='heat'),
    url(r'^external/(?P<path>.*)$', 'point_store.views.proxy', name="proxy"),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)