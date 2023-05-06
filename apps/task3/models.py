from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class Product(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    marja = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    package_code = models.CharField(max_length=255, verbose_name=_("Package Code"), null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
