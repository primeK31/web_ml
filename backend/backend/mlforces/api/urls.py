from django.urls import include, path
from api.views import task_list, get_task, task_solution, task_comment
from api.views import TaskListCreateAPIView, TaskDetailAPIView
from api.views import TaskListCreate, TaskDetail, SolutionListCreate, SolutionDetail, CommentListCreate, CommentDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('tasks/', TaskListCreate.as_view()),
    path('tasks/<int:pk>', TaskDetail.as_view()),

    path('solutions/', SolutionListCreate.as_view()),
    path('solutions/<int:pk>', SolutionDetail.as_view()),
    path('tasks/<int:pk>/solutions', task_solution),

    path('comments/', CommentListCreate.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('tasks/<int:pk>/comments', task_comment),
]
