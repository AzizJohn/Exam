from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


# Create your models here.

class Vacancy(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    salary = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    salary_from = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)
    salary_to = models.DecimalField(max_digits=12, decimal_places=2, default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.salary}'

    class Meta:
        verbose_name = _("Vacancy")
        verbose_name_plural = _("Vacancies")
