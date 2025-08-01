from django.db import models
from django.utils.translation import gettext_lazy as _

from core.apps.shared.models import BaseModel
from core.apps.products.models import Product, Unity
from core.apps.projects.models import Project, ProjectDepartment
from core.apps.accounts.models import User
from core.apps.wherehouse.models import WhereHouse


class Order(BaseModel):
    STATUS = (
        ('NEW', 'yangi'),
        ('CANCELLED', "bekor qilindi"),
        ('ACCEPTED', 'qabul qilindi'),
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='orders'
    )
    unity = models.ForeignKey(
        Unity, on_delete=models.CASCADE, related_name='orders'
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='orders'
    )
    project_department = models.ForeignKey(
        ProjectDepartment, on_delete=models.DO_NOTHING, null=True, blank=True
    )
    wherehouse = models.ForeignKey(
        WhereHouse, on_delete=models.CASCADE, related_name='orders'
    )
    date = models.DateField()
    quantity = models.PositiveBigIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS, default="NEW")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True)

    def __str__(self):
        return f"{self.product} {self.unity} quantity order"
    
    class Meta:
        verbose_name = _("Buyurtma")
        verbose_name_plural = _("Buyurtmalar")


class OrderApplication(BaseModel):
    STATUS = (
        ('NEW', 'yangi'),
        ('CANCELLED', "bekor qilindi"),
        ('ACCEPTED', 'qabul qilindi'),
    )

    orders = models.ManyToManyField(Order, related_name="applications")
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f"{self.employee} application"
    
    class Meta:
        verbose_name = _("Ariza")
        verbose_name_plural = _("Arizalar")