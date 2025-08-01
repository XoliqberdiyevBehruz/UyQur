from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.shared.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('Kompaniya')
        verbose_name_plural = _("Kompaniyalar")