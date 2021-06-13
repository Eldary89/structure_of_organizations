from django.contrib import admin
from .models import Employee, EmployeeDepartmentRelation, Position

admin.site.register([
    Employee,
    EmployeeDepartmentRelation,
    Position
])
