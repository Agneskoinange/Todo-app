from rest_framework import generics, authentication, permissions
from .models import TodoItem
from .serializers import TodoItemSerializer
from django.contrib.auth.models import User
from rest_framework.response import Response


class TodoItemListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]
  
class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Both username and password are required'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except Exception as e:
            return Response({'error': str(e)})
        return Response({'success': 'User created successfully'})
