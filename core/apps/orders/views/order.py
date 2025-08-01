from rest_framework import generics, status
from rest_framework.response import Response

from core.apps.orders.serializers import order as serializers
from core.apps.orders.models import Order
from core.apps.accounts.permissions.permissions import HasRolePermission
from core.apps.shared.paginations.custom import CustomPageNumberPagination


class OrderListApiView(generics.ListAPIView):
    serializer_class = serializers.OrderListSerializer
    queryset = Order.objects.select_related(
        'product', 'unity', 'project', 'project_department', 'wherehouse'
    )
    permission_classes = [HasRolePermission]
    required_permissions = []
    pagination_class = CustomPageNumberPagination