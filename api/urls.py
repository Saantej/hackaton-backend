from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()

routers = [
    *router.urls,
]

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/', views.KanbanView.as_view(), name='task-kanban'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/assign/', views.TaskUpdateAssignView.as_view(), name='task-assign'),  
    path('profile/', views.UserProfileView.as_view(), name='user-profile'),  
]
