from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^test_lehestik/', include('test_lehestik.urls')),
    url(r'^app/', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]
