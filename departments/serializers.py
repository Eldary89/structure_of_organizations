from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Department, DepartmentCatalog
from organizations.serializers import OrganizationSerializer
from employees.serializers import EmployeeSerializer


class DepartmentCatalogSerializer(ModelSerializer):
    class Meta:
        model = DepartmentCatalog
        fields = '__all__'


class DepartmentSerializer(ModelSerializer):
    department_name = serializers.CharField(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    co_department = serializers.SerializerMethodField(read_only=True)
    head_of_department = serializers.SerializerMethodField(read_only=True)

    def get_co_department(self, obj: Department):
        return DepartmentSerializer(obj.co_department, read_only=True).data

    def get_head_of_department(self, obj: Department):
        if obj.head_of_department is not None:
            return EmployeeSerializer(obj.head_of_department.employee, read_only=True).data
        else:
            return None

    class Meta:
        model = Department
        fields = '__all__'
