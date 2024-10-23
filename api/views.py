from rest_framework import generics
from rest_framework.permissions import AllowAny
from . import serializers
from django.contrib.auth import get_user_model
from .serializers import *
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import EmailTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from core.models import Task
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from django.db.models import Case, When, Value, IntegerField
from collections import defaultdict

User = get_user_model()


class FeedbackRequestCreateView(generics.CreateAPIView):
    serializer_class = FeedbackRequestSerializer
    permission_classes = (AllowAny,)



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

class EmailTokenObtainPairView(generics.GenericAPIView):
    serializer_class = EmailTokenObtainPairSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class TaskUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()
        


class KanbanView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        status_order = Case(
            When(status='backlog', then=Value(1)),
            When(status='in_progress', then=Value(2)),
            When(status='ready_to_test', then=Value(3)),
            When(status='done', then=Value(4)),
            When(status='blocked', then=Value(5)),
            output_field=IntegerField(),
        )
        
        queryset = Task.objects.all().order_by(status_order, 'created_at')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        grouped_tasks = defaultdict(list)
        for task in queryset:
            grouped_tasks[task.status].append(TaskSerializer(task).data)

        return Response(dict(grouped_tasks))
        
        
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
class TaskUpdateAssignView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        task = self.get_object()  
        assigned_to_ids = request.data.get('assigned_to', [])
        users = User.objects.filter(id__in=assigned_to_ids) 
        
        task.assigned_to.set(users)
        task.save()

        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user