import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class TicketsClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/tickets"
        self.max_threads = 5  # Controla o número de requisições simultâneas

    def fetch_page(self, params):
        """Faz uma requisição para uma página da API do Zendesk e trata rate limits."""
        response = self.request("GET", self.endpoint, params=params)
        tickets = response.get("tickets", [])
        meta = response.get("meta", {})

        # Monitorando rate limit
        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return tickets, meta.get("after_cursor"), meta.get("has_more", False)

    def get_all_tickets(self):
        """Busca todos os tickets paginados usando ThreadPoolExecutor."""
        all_tickets = []
        pages_to_fetch = []
        params = {}

        # Primeira requisição para pegar o cursor inicial
        tickets, after_cursor, has_more = self.fetch_page(params)
        all_tickets.extend(tickets)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())

            # Atualiza o cursor para a próxima página
            _, after_cursor, has_more = self.fetch_page(params)

        # Usa ThreadPoolExecutor para coletar múltiplas páginas em paralelo
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                tickets, _, _ = future.result()
                all_tickets.extend(tickets)

        # Converte os tickets para um DataFrame pandas
        df = pd.DataFrame(all_tickets)
        return df
