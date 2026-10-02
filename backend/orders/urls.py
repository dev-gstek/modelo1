from django.urls import path
from .views import FinancialDashboardAPIView

urlpatterns = [
    path('api/v1/dashboard/financials/', FinancialDashboardAPIView.as_view(), name='api-financials'),
]
