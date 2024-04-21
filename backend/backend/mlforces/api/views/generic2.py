from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

from api.models import Solution, Comment
from api.serializers import SolutionSerializer2, CommentSerializer2

class SolutionListCreate(generics.ListCreateAPIView):  # get, post
    permission_classes = (IsAuthenticated,)
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2

class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):  # get, put, delete
    permission_classes = (IsAuthenticated,)
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2

class CommentListCreate(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer2

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer2
