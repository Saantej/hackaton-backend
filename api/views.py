from django.contrib.redirects.models import Redirect
from rest_framework import generics
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from _project_ import constants
from core import models as core_models
from integrations.bitrix import actions as bitrix_actions

from . import serializers


class TextPageViewSet(ModelViewSet):

    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    serializer_class = serializers.TextPageSerializer
    queryset = core_models.TextPage.objects.all()


class RedirectsViewSet(ModelViewSet):

    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, )

    serializer_class = serializers.RedirectSerializer
    queryset = Redirect.objects.all()


class FeedbackRequestCreateView(generics.CreateAPIView):
    serializer_class = serializers.FeedbackRequestSerializer
    permission_classes = ()

    def perform_create(self, serializer):
        instance = serializer.save()

        utm_dict = self.request._request.session.get(constants.SessionKeys.UTM.value, {})
        bitrix_actions.create_lead(
            instance.first_name,
            instance.last_name,
            instance.email,
            instance.phone,
            **utm_dict
        )
