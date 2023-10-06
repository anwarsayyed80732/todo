from django_filters.rest_framework import DjangoFilterBackend
from .serializers import todoserializer
from .models import todo
from rest_framework import viewsets, filters

class todoviewset(viewsets.ModelViewSet):
    queryset=todo.objects.all()
    serializer_class=todoserializer
    filter_backends=[
        DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter
    ]

filterset_fields=("title","user","is_complete")
search_fields=("title")
ordering_fields=("is_complete","created_At","updated_At")



# Create your views here.
