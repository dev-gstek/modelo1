from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import FinancialDashboardSerializer

class FinancialDashboardAPIView(generics.ListAPIView):
    """
    Endpoint que alimenta a tabela e o dashboard do frontend.
    Puxa os pedidos com seus cálculos financeiros completos.
    """
    queryset = Order.objects.select_related('marketplace').prefetch_related('items__product').order_by('-order_date')
    serializer_class = FinancialDashboardSerializer


class MercadoLivreWebhookView(APIView):
    """
    Recebe os pings (notificações) em tempo real do Mercado Livre.
    Quando uma venda acontece, o ML bate aqui e nós mandamos o Celery buscar.
    """
    def post(self, request, *args, **kwargs):
        payload = request.data
        topic = payload.get("topic")
        
        # Se for um alerta de pedido novo/pago, engatilha o motor de sincronização
        if topic == "orders_v2":
            # Poderíamos acionar uma task específica passando o ID do pedido:
            # resource_url = payload.get("resource")
            # sync_single_mercadolivre_order.delay(resource_url)
            
            # Para simplificar o fluxo arquitetural:
            from orders.tasks import sync_mercadolivre_orders
            sync_mercadolivre_orders.delay()
            
        return Response({"status": "received"}, status=status.HTTP_200_OK)
