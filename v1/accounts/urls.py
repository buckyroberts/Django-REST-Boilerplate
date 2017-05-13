from django.conf.urls import url
from .views.user import UserView


urlpatterns = [

    # Users
    url(r'^users$', UserView.as_view()),

]
