from dango.urls import path
from .views import TodoListView, TodoCreateView, TodoDetailView, TodoUpdateView, TodoDeleteView


urlpatterns = [
    path('', TodoListView.as_view(), name='todo_list'),
    path('<int:pk>', TodoDetailView.as_view(), name='todo_detail'),
    path('create/', TodoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete/', TodoDeleteView.as_view(), name='todo_delete'),
    path('api/', TodoItemListView.as_view(), name='api_todo_list'),
    path('api/<int:pk>/', TodoItemDetailView.as_view(), name='api_todo_detail'),
    
]