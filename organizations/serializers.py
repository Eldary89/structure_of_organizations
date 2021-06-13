from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Organization


class OrganizationSerializer(ModelSerializer):
    co_organizations = serializers.SerializerMethodField(read_only=True)

    def get_co_organizations(self, obj: Organization):
        return OrganizationSerializer(obj.co_organizations.all(), many=True).data

    class Meta:
        model = Organization
        fields = '__all__'
