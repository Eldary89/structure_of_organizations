from django.db import models
from common.models import BaseModel, BaseCatalog


class Organization(BaseModel):
    name = models.CharField(
        max_length=1000,
        verbose_name="Название организации"
    )
    co_organizations = models.ManyToManyField(
        'organizations.Organization',
        blank=True,
        verbose_name="Является дочерней организаций"
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
