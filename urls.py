from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('stripetest.views',
    url(r'stripetest/$', 'index'),
    url(r'stripetest/products/$', 'products'),
)
