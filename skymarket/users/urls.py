from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
    # path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/token/verify/', TokenVerifyView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view()),
]
