from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import TodoSerializer
from rest_framework import status

@api_view(['GET'])
def TodoView(request):
	api_urls = {
		'READ all': '/',
		'READ one': '/?title=title_name',
		'CREATE': '/create',
		'UPDATE': '/update/pk',
		'DELETE': '/todolist/pk/delete'
	}

	return Response(api_urls)

@api_view(['POST'])
def add_todo(request):
    serializer = TodoSerializer(data=request.data)
  
    if serializer.is_valid():
        serializer.save(created_by=request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        return Response({"status": "Error", "reason": serializer.errors},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_todo(request):
    todo = Todolist.objects.all()
    serializer = TodoSerializer(todo, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def view_one(request, pk):
    todo = Todolist.objects.get(id=pk)
    serializer = TodoSerializer(todo, many = False)
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request, pk):
    todo = Todolist.objects.get(id = pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todolist.objects.get(id = pk)
    todo.delete()
    return Response("Taks deleted successfully.")
