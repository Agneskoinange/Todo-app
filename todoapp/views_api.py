from rest_framework import generics, viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer

class TodoItemListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
  
class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
  
