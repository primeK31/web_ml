from rest_framework import serializers
from .models import Task, Solution, Comment, Profile

from django.contrib.auth.models import User


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    statement = serializers.CharField()

    def create(self, validated_data):
        instance = Task(name=validated_data.get('name'), statement=validated_data.get('statement'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.statement = validated_data.get('statement')
        instance.save()
        return instance


class TaskSerializer2(serializers.ModelSerializer):
    name = serializers.CharField()
    statement = serializers.CharField()
    start_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ('id', 'name', 'statement', 'start_time', 'author')


class SolutionSerializer2(serializers.ModelSerializer):
    content = serializers.CharField()
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Solution
        fields = ('id', 'content', 'task')


class CommentSerializer2(serializers.ModelSerializer):
    content = serializers.CharField()
    votes = serializers.IntegerField()

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'content', 'votes', 'user_id', 'task')
