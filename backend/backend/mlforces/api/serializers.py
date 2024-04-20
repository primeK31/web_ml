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


class ProfileSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    bio = serializers.CharField()
    points = serializers.IntegerField()

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        instance = Profile(bio=validated_data.get('bio'), points=validated_data.get('points'), user=validated_data.get('user'))
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.bio = validated_data.get("bio")
        instance.points = validated_data.get('points')
        instance.user = validated_data.get('user')
        instance.save()
        return instance


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class SolutionSerializer2(serializers.ModelSerializer):
    content = serializers.CharField()
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())
    points = serializers.IntegerField()

    class Meta:
        model = Solution
        fields = ('id', 'content', 'task', 'points')


class CommentSerializer2(serializers.ModelSerializer):
    content = serializers.CharField()
    votes = serializers.IntegerField()

    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Comment
        fields = ('id', 'content', 'votes', 'user_id', 'task')
