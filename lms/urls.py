from django.urls import path
from rest_framework.routers import SimpleRouter

from lms.apps import LmsConfig
from lms.views import (
    CourseViewSet,
    LessonCreateApiView,
    LessonListApiView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    SubscriptionCreateAPIView,
    SubscriptionListAPIView,
)

app_name = LmsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListApiView.as_view(), name="Lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="Lesson_retrieve"),
    path("lesson/create/", LessonCreateApiView.as_view(), name="Lesson_create"),
    path("lesson/<int:pk>/destroy/",LessonDestroyAPIView.as_view(),name="Lesson_destroy",),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="Lesson_update"),
    path("subscription/create/", SubscriptionCreateAPIView.as_view(), name="subscription_create"),
    path("subscription/", SubscriptionListAPIView.as_view(), name="subscriptions"),
]

urlpatterns += router.urls