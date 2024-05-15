import pdb

from django.contrib.redirects.models import Redirect
from rest_framework import generics, status
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from _project_ import constants
from core import models as core_models
from integrations.bitrix import actions as bitrix_actions

from . import serializers


class TextPageViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    serializer_class = serializers.TextPageSerializer
    queryset = core_models.TextPage.objects.all()


class RedirectsViewSet(ModelViewSet):
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)

    serializer_class = serializers.RedirectSerializer
    queryset = Redirect.objects.all()


class FeedbackRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.FeedbackRequestSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.first_name and instance.phone:
            bitrix_actions.create_lead(
                instance.first_name,
                instance.phone,
            )
        return Response(status=status.HTTP_200_OK)
