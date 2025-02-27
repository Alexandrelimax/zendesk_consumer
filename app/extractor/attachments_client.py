import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class AttachmentsClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/attachments"
        self.max_threads = 5

    def fetch_page(self, params):
        response = self.request("GET", self.endpoint, params=params)
        attachments = response.get("attachments", [])
        meta = response.get("meta", {})

        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return attachments, meta.get("after_cursor"), meta.get("has_more", False)

    def get_all_attachments(self):
        all_attachments = []
        pages_to_fetch = []
        params = {}

        attachments, after_cursor, has_more = self.fetch_page(params)
        all_attachments.extend(attachments)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())
            _, after_cursor, has_more = self.fetch_page(params)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                attachments, _, _ = future.result()
                all_attachments.extend(attachments)

        df = pd.DataFrame(all_attachments)
        return df
