from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Department, DepartmentCatalog
from .serializers import DepartmentSerializer


class DepartmentViewSet(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
