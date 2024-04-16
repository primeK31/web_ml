from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=255)
    statement = models.TextField()

    def __str__(self):
        return self.name

    def to_json(self):
        return {'name': self.name, 'statement': self.statement}


class Solution(models.Model):
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="solutions")

    def __str__(self):
        return self.content

    def to_json(self):
        return {'content': self.content, 'task': self.task.id }

