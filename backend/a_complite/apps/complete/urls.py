from django.conf.urls import url
from .views import BookByFieldListView, BookController, AuthorController, PublisherController
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    url(r'complete/$', BookByFieldListView.as_view()),
    url(r'book/$', BookController.as_view()),
    url(r'author/$', AuthorController.as_view()),
    url(r'publisher/$', PublisherController.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
