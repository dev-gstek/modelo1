import requests
import logging

logger = logging.getLogger(__name__)

class NuvemShopClient:
    def __init__(self, marketplace):
        self.marketplace = marketplace
        self.creds = marketplace.api_credentials or {}
        self.access_token = self.creds.get('access_token')
        self.user_id = self.creds.get('user_id')
        self.base_url = f"https://api.nuvemshop.com.br/v1/{self.user_id}"

    def fetch_recent_orders(self):
        """
        Fase 3: Captura de Pedidos Reais da NuvemShop.
        """
        if not self.access_token or not self.user_id:
            logger.error("Credenciais NuvemShop incompletas.")
            return []

        headers = {
            "Authentication": f"bearer {self.access_token}",
            "User-Agent": "DomLux ERP (seu_email@gstek.com)"
        }
        
        url = f"{self.base_url}/orders?status=paid"
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Erro ao buscar pedidos da NuvemShop: {response.text}")
            return []
