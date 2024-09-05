from rest_framework import generics
from rest_framework.permissions import AllowAny

from . import serializers


class FeedbackRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.FeedbackRequestSerializer
    permission_classes = (AllowAny,)
