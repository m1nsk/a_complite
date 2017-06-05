from django.conf.urls import url
from .views import BookByAuthorListView, BookByPublisherListView
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'author/(?P<complete_author>(.)+)/$', BookByAuthorListView.as_view()),
    url(r'publisher/(?P<complete_publisher>(.)+)/$', BookByPublisherListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
