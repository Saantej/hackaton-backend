from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

routers = [
    *router.urls,
]

urlpatterns = [
    path('', include("knox.urls")),
    path('feedback-request/', views.FeedbackRequestCreateView.as_view(), name="api-feedbackrequest-list"),
    *router.urls
]
