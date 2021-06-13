from django.contrib import admin
from .models import Department, DepartmentCatalog

admin.site.register([
    Department,
    DepartmentCatalog,
])
