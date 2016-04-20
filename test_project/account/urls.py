from django.conf.urls import url
from account.views import profile

urlpatterns = [
    url(r'^profile/$', profile, name='profile'),
]
