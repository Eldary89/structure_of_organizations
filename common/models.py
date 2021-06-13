from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    uid = models.UUIDField(
        verbose_name="Уникальный идентификатор",
        primary_key=True,
        editable=False,
        default=uuid4,
        unique=True,
    )
    is_active = models.BooleanField(
        default=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return super().__str__()

    class Meta:
        abstract = True


class BaseCatalog(BaseModel):
    name = models.CharField(
        max_length=1000,
        verbose_name="Название"
    )
    code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True
