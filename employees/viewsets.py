from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import EmployeeDepartmentRelation, Employee, Position
from .serializers import PositionSerializer, EmployeeSerializer, FullEmployeeSerializer


class PositionsViewSet(ReadOnlyModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class EmployeeViewSet(ReadOnlyModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset().get(uid=kwargs.get('pk'))
        serializer = FullEmployeeSerializer(queryset).data
        return Response(serializer, status=status.HTTP_200_OK)
