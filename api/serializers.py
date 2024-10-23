from django.contrib.redirects.models import Redirect
from rest_framework import serializers
from core import models
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class TextPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextPage
        fields = ("name", "content", "slug", "show_in_sitemap", "og_title",
                  "og_description", "og_type", "og_type_pb_time", "og_type_author",
                  "seo_h1", "seo_title", "seo_description", "seo_keywords",)


class RedirectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Redirect
        fields = ("site", "old_path", "new_path")


class FeedbackRequestSerializer(serializers.ModelSerializer):
    test = serializers.CharField(required=False, allow_blank=True, read_only=True)

    class Meta:
        model = models.FeedbackRequest
        fields = ("first_name", "phone", "company_name", "message", 'test')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, help_text="Пароль для нового пользователя")
    email = serializers.EmailField(help_text="Электронная почта пользователя")

    class Meta:
        model = User
        fields = ('password', 'email')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        
class EmailTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, help_text="Электронная почта для авторизации")
    password = serializers.CharField(write_only=True, help_text="Пароль для авторизации")

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email:
            raise serializers.ValidationError({'email': 'Это поле обязательно.'})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'email': 'Пользователь с таким email не найден.'})

        if not user.check_password(password):
            raise serializers.ValidationError({'password': 'Неверный пароль.'})

        refresh = TokenObtainPairSerializer.get_token(user)

        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(read_only=True, help_text="Создатель задачи")
    assigned_to = UserSerializer(many=True, read_only=True, help_text="Исполнители задачи")
    title = serializers.CharField(help_text="Название задачи")
    description = serializers.CharField(help_text="Описание задачи")
    status = serializers.ChoiceField(choices=[('backlog', 'Backlog'), ('blocked', 'Blocked'), ('in_progress', 'В процессе'), ('ready_to_test', 'Готово к тестированию'), ('done', 'Завершено')], help_text="Статус задачи")

    class Meta:
        model = models.Task
        fields = ['id', 'title', 'description', 'status', 'created_by', 'assigned_to', 'start_date', 'end_date', 'created_at', 'updated_at']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'surname', 'email', 'phone_number', 'profile_picture', 'birth_date', 'country']
        read_only_fields = ['email']