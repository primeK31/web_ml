import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializer, TaskSerializer2, UserBasicSerializer

from django.contrib.auth.models import User


class UserListAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserBasicSerializer(users, many=True)
        return Response(serializer.data)


class UserDetailView(APIView):
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserBasicSerializer(user)
        return Response(serializer.data)


class TaskListCreateAPIView(APIView):
    def get(self, request):
        categories = Task.objects.all()
        serializer = TaskSerializer2(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):

    def get_object(self, pk=None):
        try:
            category = Task.objects.get(id=pk)
            return category
        except Task.DoesNotExist as e:
            return Response({"error": str(e)})

    def get(self, request, pk=None):
        category = self.get_object(pk)

        serializer = TaskSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk=None):
        category = self.get_object(pk)

        serializer = TaskSerializer2(
            instance=category,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        category = self.get_object(pk)

        category.delete()
        return Response({"deleted": True})
