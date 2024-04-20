from django.urls import path
from api.views import task_list, get_task, task_solution, task_comment, get_profile
from api.views import UserDetailView, UserListAPIView
from api.views import SolutionListCreate, SolutionDetail, CommentListCreate, CommentDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('tasks/', task_list),
    path('tasks/<int:pk>', get_task),

    path('solutions/', SolutionListCreate.as_view()),
    path('solutions/<int:pk>', SolutionDetail.as_view()),
    path('tasks/<int:pk>/solutions', task_solution),

    path('comments/', CommentListCreate.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('tasks/<int:pk>/comments', task_comment),

    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>', UserDetailView.as_view()),

    path('profiles/<int:pk>', get_profile),
]
