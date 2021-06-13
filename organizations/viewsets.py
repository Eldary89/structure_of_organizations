from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Organization
from .serializers import OrganizationSerializer


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer