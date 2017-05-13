from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.documentation import include_docs_urls


urlpatterns = [

    # Core
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Django REST Boilerplate')),

    # API (v1)
    url(r'^', include('v1.accounts.urls')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
