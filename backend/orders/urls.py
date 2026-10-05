from django.urls import path
from .views import FinancialDashboardAPIView, MercadoLivreWebhookView

urlpatterns = [
    path('api/v1/dashboard/financials/', FinancialDashboardAPIView.as_view(), name='api-financials'),
    path('api/webhooks/mercadolivre/', MercadoLivreWebhookView.as_view(), name='webhook-ml'),
]
