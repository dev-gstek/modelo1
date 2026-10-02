from rest_framework import generics
from .models import Order
from .serializers import FinancialDashboardSerializer

class FinancialDashboardAPIView(generics.ListAPIView):
    """
    Endpoint que alimenta a tabela e o dashboard do frontend.
    Puxa os pedidos com seus cálculos financeiros completos.
    """
    queryset = Order.objects.select_related('marketplace').prefetch_related('items__product').order_by('-order_date')
    serializer_class = FinancialDashboardSerializer
