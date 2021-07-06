from django.conf.urls import url
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.pictures,name='pictures'),
    url(r'^search/',views.search_results,name = 'search_results'),
    url('location/(?P<location>\w+)',views.locations,name = 'location'),
    url(r'^location/(\d+)',views.locations,name='location'),
    ]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)