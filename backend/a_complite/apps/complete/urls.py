from django.conf.urls import url
from .views import BookByFieldListView, PublisherViewSet, AuthorViewSet, BookViewSet, PublisherByFieldListView, AuthorByFieldListView, BookByFieldsIdListView
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

router = DefaultRouter()
router.register(r'publisher', PublisherViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'book', BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'complete/book$', BookByFieldListView.as_view()),
    url(r'complete/publisher$', PublisherByFieldListView.as_view()),
    url(r'complete/author$', AuthorByFieldListView.as_view()),
    url(r'complete/idlist$', BookByFieldsIdListView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
