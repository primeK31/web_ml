from rest_framework import mixins, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Task
from api.serializers import TaskSerializer, TaskSerializer2


class TaskListCreate(mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class TaskDetail(mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.GenericAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer2

    def get(self, request, pk=None):
        return self.retrieve(request, pk)

    def put(self, request, pk=None):
        return self.update(request, pk)

    def delete(self, request, pk=None):
        return self.destroy(request, pk)