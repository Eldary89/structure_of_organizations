from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Employee, EmployeeDepartmentRelation, Position


class PositionSerializer(ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    first_name = serializers.SerializerMethodField(read_only=True)
    last_name = serializers.SerializerMethodField(read_only=True)

    def get_first_name(self, obj: Employee):
        return obj.user.first_name

    def get_last_name(self, obj: Employee):
        return obj.user.last_name

    class Meta:
        model = Employee
        fields = [
            'first_name',
            'last_name',
            'uid',
            'created',
        ]


class EmployeeDepartmentRelationSerializer(ModelSerializer):
    department = serializers.CharField(read_only=True)
    position = serializers.CharField(read_only=True)

    class Meta:
        model = EmployeeDepartmentRelation
        fields = [
            "department",
            'position',
            'created'
        ]


class FullEmployeeSerializer(EmployeeSerializer):
    def to_representation(self, instance: Employee):
        data = super(FullEmployeeSerializer, self).to_representation(instance)
        data["departments"] = EmployeeDepartmentRelationSerializer(
            instance.employeedepartmentrelation_set.all(), many=True).data
        return data
