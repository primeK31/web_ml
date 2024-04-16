from django.urls import include, path
from api.views import task_list, get_task, task_solution
from api.views import TaskListCreateAPIView, TaskDetailAPIView
from api.views import TaskListCreate, TaskDetail, SolutionListCreate, SolutionDetail


urlpatterns = [
    path('tasks/', TaskListCreate.as_view()),
    path('tasks/<int:pk>', TaskDetail.as_view()),
    path('solutions/', SolutionListCreate.as_view()),
    path('solutions/<int:pk>', SolutionDetail.as_view()),
    path('tasks/<int:pk>/solutions', task_solution),
]
