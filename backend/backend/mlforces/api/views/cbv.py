from rest_framework.views import APIView
from rest_framework.response import Response

from api.serializers import UserBasicSerializer

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

