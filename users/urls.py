from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.apps import UsersConfig
from users.views import (
    UserViewSet,
    PaymentListCreateAPIView,
    PaymentRetrieveUpdateDestroyAPIView,
    UserCreateAPIView,
    PaymentCreateAPIView
)


app_name = UsersConfig.name

router = SimpleRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("payment/", PaymentListCreateAPIView.as_view(), name="payment_detail"),
    path("create/payment/", PaymentCreateAPIView.as_view(), name="create_payment"),
    path("payment/<int:pk>/", PaymentRetrieveUpdateDestroyAPIView.as_view(), name="payment_detail"),
    path("login/", TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(permission_classes=(AllowAny,)), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
] + router.urls