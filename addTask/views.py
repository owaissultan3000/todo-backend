from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404


# Create your views here.

class TaskViews(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            # item = Task.objects.get()
            # serializer = TaskSerializer(item)
            items = Task.objects.all()
            
            serializer = TaskSerializer(items, many=True)
            data = {}
            i=0
            for task in serializer.data:
                if str(id) == str(task['userid']):
                    i += 1
                    data['task' + str(i)] = dict(task)       
            return Response({"status": "success", "data": data}, status=status.HTTP_200_OK)

        items = Task.objects.all()
        serializer = TaskSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(Task, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})    

        

