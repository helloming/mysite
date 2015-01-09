from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
from .views import hello,current_datetime,hours_ahead,search_form,search

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #hello test
    url(r'^hello/$', hello),
    url(r'^timenow/$', current_datetime),
    url(r'^time/plus/(\d{1,2})$', hours_ahead),
    url(r'^search-form/$', search_form),
    url(r'^search/$', search)

)



