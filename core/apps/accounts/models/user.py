from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.apps.shared.models import BaseModel
from core.apps.accounts.models.role import Role


class User(BaseModel, AbstractUser):
    profile_image = models.ImageField(
        upload_to="users/profile_images/", null=True, blank=True, verbose_name=_('profil rasmi')
    )
    role = models.ForeignKey(Role, on_delete=models.DO_NOTHING, null=True, related_name="users")

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = _("Foydalanuvchi")
        verbose_name_plural = _("Foydalanuvchilar")
