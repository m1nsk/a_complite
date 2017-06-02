from django.conf.urls import url
from .views import author_list, publisher_list

urlpatterns = [
    url(r'author/(?P<complete_author>(.)+)/$', author_list),
    url(r'publisher/(?P<complete_publisher>(.)+)/$', publisher_list),
]
