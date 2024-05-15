from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.SimpleRouter()
router.register(r"textpage", views.TextPageViewSet)
router.register(r"redirect", views.RedirectsViewSet)

urlpatterns = [
    path('', include("knox.urls")),
    path('feedback-request/', views.FeedbackRequestCreateView.as_view(), name="api-feedbackrequest-list"),
] + router.urls
