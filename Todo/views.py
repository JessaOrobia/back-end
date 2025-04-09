# todo/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TodoItem
from .serializers import TodoSerializer  

@api_view(['GET'])
def todo_list(request):
    todos = TodoItem.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PATCH', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = TodoItem.objects.get(pk=pk)
    except TodoItem.DoesNotExist:
        return Response({'error': 'Todo not found'}, status=404)

    if request.method == 'PATCH':
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'Deleted successfully'}, status=204)