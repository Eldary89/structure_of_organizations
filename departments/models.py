from django.db import models
from common.models import BaseModel, BaseCatalog
from organizations.models import Organization


class DepartmentCatalog(BaseCatalog):
    class Meta:
        verbose_name = "Наименование департамента"
        verbose_name_plural = "Наименования департаментов"


class Department(BaseModel):
    department_name = models.ForeignKey(
        DepartmentCatalog,
        on_delete=models.CASCADE,
        verbose_name="Наименование департамента"
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        verbose_name="Организация"
    )
    co_department = models.ForeignKey(
        'departments.Department',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Является дочерним департаментом"
    )
    head_of_department = models.ForeignKey(
        'employees.EmployeeDepartmentRelation',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Глава департамента",
        related_name="head_of_department_set"
    )

    class Meta:
        verbose_name = "Департамент"
        verbose_name_plural = "Департаменты"

    def __str__(self):
        if self.co_department is not None:
            return f"{self.department_name.name} при {self.co_department}"
        else:
            return f"{self.department_name.name} при {self.organization}"
