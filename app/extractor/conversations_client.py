import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class ConversationsClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/conversations"
        self.max_threads = 5

    def fetch_page(self, params):
        response = self.request("GET", self.endpoint, params=params)
        conversations = response.get("conversations", [])
        meta = response.get("meta", {})

        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return conversations, meta.get("after_cursor"), meta.get("has_more", False)

    def get_all_conversations(self):
        all_conversations = []
        pages_to_fetch = []
        params = {}

        conversations, after_cursor, has_more = self.fetch_page(params)
        all_conversations.extend(conversations)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())
            _, after_cursor, has_more = self.fetch_page(params)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                conversations, _, _ = future.result()
                all_conversations.extend(conversations)

        df = pd.DataFrame(all_conversations)
        return df
