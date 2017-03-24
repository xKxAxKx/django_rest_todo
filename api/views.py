from rest_framework.viewsets import ModelViewSet
from .models import Todo
from .serializers import TodoSerializer
import os
from django.conf import settings
from django.http.response import HttpResponse

def index(_):
    html = open(
        os.path.join(settings.STATICFILES_DIRS[0], "index.html")).read()
    return HttpResponse(html)

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
