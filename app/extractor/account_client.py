import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class AccountClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/account"
        self.max_threads = 5  # Definindo um número razoável de threads

    def fetch_page(self, params):
        """Faz uma requisição para a API do Zendesk e trata rate limits."""
        response = self.request("GET", self.endpoint, params=params)
        account = response.get("account", {})  # A API de Account geralmente retorna um único objeto
        meta = response.get("meta", {})

        # Monitorando rate limit (caso exista)
        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return [account], meta.get("after_cursor"), meta.get("has_more", False)

    def get_account_info(self):
        """Obtém as informações da conta do Zendesk e retorna como DataFrame."""
        all_data = []
        pages_to_fetch = []
        params = {}

        # Faz a primeira requisição
        account, after_cursor, has_more = self.fetch_page(params)
        all_data.extend(account)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())
            _, after_cursor, has_more = self.fetch_page(params)

        # Usa ThreadPoolExecutor para otimizar a busca
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                account, _, _ = future.result()
                all_data.extend(account)

        # Converte para DataFrame
        df = pd.DataFrame(all_data)
        return df
