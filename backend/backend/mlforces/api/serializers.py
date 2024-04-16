from rest_framework import serializers
from .models import Task, Solution


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

    class Meta:
        model = Task
        fields = ('id', 'name', 'statement')


class SolutionSerializer2(serializers.ModelSerializer):
    content = serializers.CharField()
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all())

    class Meta:
        model = Solution
        fields = ('id', 'content', 'task')
