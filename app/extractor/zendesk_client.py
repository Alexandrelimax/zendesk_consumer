import requests
import os
from app.client.exceptions import ZendeskAPIException

class ZendeskClient:
    def __init__(self):
        self.base_url = os.getenv("ZENDESK_BASE_URL")
        self.api_token = os.getenv("ZENDESK_API_TOKEN")
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        })

    def request(self, method: str, endpoint: str, params=None, data=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.request(method, url, params=params, json=data)

        if not response.ok:
            raise ZendeskAPIException(response)

        return response.json()
