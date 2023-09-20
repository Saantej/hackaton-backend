from django.contrib.redirects.models import Redirect

from rest_framework import serializers

from core import models


class TextPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TextPage
        fields = ("name", "content", "slug", "show_in_sitemap", "og_title",
                  "og_description", "og_type", "og_type_pb_time", "og_type_author",
                  "seo_h1", "seo_title", "seo_description", "seo_keywords", )


class RedirectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Redirect
        fields = ("site", "old_path", "new_path")


class FeedbackRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.FeedbackRequest
        fields = ("email", "first_name", "last_name", "phone", "comment",)
