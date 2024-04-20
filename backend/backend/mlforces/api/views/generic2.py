from rest_framework import generics

from api.models import Solution, Comment
from api.serializers import SolutionSerializer2, CommentSerializer2


class SolutionListCreate(generics.ListCreateAPIView): # get, post
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView): # get, put, delete
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer2


class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer2


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer2
