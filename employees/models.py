from django.db import models
from common.models import BaseModel, BaseCatalog
from departments.models import Department
from django.contrib.auth.models import User


class Employee(BaseModel):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name='employee'
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"


class Position(BaseCatalog):
    class Meta:
        verbose_name = "Наименование должности"
        verbose_name_plural = "Наименования должностей"


class EmployeeDepartmentRelation(BaseModel):
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        verbose_name="Сотрудник"
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Департамент"
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.SET_NULL,
        verbose_name="Должность",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Принадлежность сотрудника к департаменту"
        verbose_name_plural = "Принадлежность сотрудников к департаменту(ам)"

    def __str__(self):
        return f"{self.position if self.position is not None else ''} {self.employee}"
