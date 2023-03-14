from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    message = "Welcome to my Todo App!"
    return HttpResponse(message)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('todoapp/', include('todoapp.urls')),
] 
