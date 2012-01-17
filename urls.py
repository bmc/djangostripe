from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('stripetest.views',
    url(r'^stripetest/buy$', 'buy'),
    url(r'^stripetest/product/(\d+)', 'product'),
    url(r'^stripetest/$', 'index'),
    url(r'^stripetest/force_logout$', 'force_logout'),
    url(r'^/?$', 'index'),
)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {
        'url': '/static/favicon.ico'
    })
)
