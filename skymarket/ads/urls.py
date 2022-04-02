from django.conf.urls.static import static
from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, AdsImageView, AdsMine, CommentViewSet
from skymarket import settings

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet, basename="ads")
comments_router = SimpleRouter()
comments_router.register("comments", CommentViewSet, basename="comments")


urlpatterns = [
    # path("", include(ads_router.urls)),
    # path('ads/<int:pk>/upload_image/', AdsImageView.as_view()), # add method to viewset, so this is unnecessary
    path('ads/me/', AdsMine.as_view()),
    path("ads/<int:pk>/", include(comments_router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + ads_router.urls