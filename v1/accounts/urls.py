from django.conf.urls import url
from .views.test import hello


urlpatterns = [

    url(r'^hello$', hello),

]
