from django.conf.urls import url
from .views import complete_list

urlpatterns = [
    url(r'^(?P<complete_query>(.)+)/$', complete_list),
]