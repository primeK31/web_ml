from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Task, Solution
from api.serializers import TaskSerializer, TaskSerializer2, SolutionSerializer2


class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2


class SolutionListCreate(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2

