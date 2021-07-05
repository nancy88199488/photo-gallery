from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'index.html'),
    url(r'^search/', views.search_image, name='search_image'),
    url(r'^location/(\d+)', views.location_filter, name='location_filter'),
    url(r'^image/(\d+)',views.image,name = 'image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

