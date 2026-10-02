import requests
from django.utils import timezone
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

class MercadoLivreClient:
    BASE_URL = "https://api.mercadolibre.com"

    def __init__(self, marketplace):
        self.marketplace = marketplace
        self.creds = marketplace.api_credentials or {}
        self.client_id = self.creds.get('client_id')
        self.client_secret = self.creds.get('client_secret')
        self.access_token = self.creds.get('access_token')
        self.refresh_token = self.creds.get('refresh_token')
        self.seller_id = self.creds.get('seller_id')
        
    def refresh_access_token(self):
        """
        Fase 2: Autenticação Segura (OAuth 2.0).
        Renova o token se estiver expirado e salva no banco de dados.
        """
        if not self.refresh_token:
            logger.error("Sem refresh_token do ML. O cliente precisa autorizar o App primeiro.")
            return False

        url = f"{self.BASE_URL}/oauth/token"
        payload = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token
        }
        
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            data = response.json()
            self.access_token = data.get("access_token")
            self.refresh_token = data.get("refresh_token")
            
            # Atualiza o banco de dados (Marketplace)
            self.creds['access_token'] = self.access_token
            self.creds['refresh_token'] = self.refresh_token
            self.creds['token_expires_at'] = (timezone.now() + timedelta(hours=6)).isoformat()
            self.marketplace.api_credentials = self.creds
            self.marketplace.save(update_fields=['api_credentials'])
            return True
        else:
            logger.error(f"Erro ao renovar token ML: {response.text}")
            return False

    def fetch_recent_orders(self):
        """
        Fase 3: Captura de Pedidos Reais.
        """
        if not self.access_token:
            if not self.refresh_access_token():
                return []

        headers = {"Authorization": f"Bearer {self.access_token}"}
        url = f"{self.BASE_URL}/orders/search?seller={self.seller_id}&order.status=paid"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 401: # Token expirado
            if self.refresh_access_token():
                headers = {"Authorization": f"Bearer {self.access_token}"}
                response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json().get('results', [])
        else:
            logger.error(f"Erro ao buscar pedidos do ML: {response.text}")
            return []
