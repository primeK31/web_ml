import json
from django.http import JsonResponse
from api.models import Task
from api.serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task_list(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        data = json.loads(request.body)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def get_task(request, pk=None):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data = json.loads(request.body)
        serializer = TaskSerializer(
            instance=task,
            data=data
        )
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse({"deleted": True})

    return JsonResponse({'id': 'pk'})
