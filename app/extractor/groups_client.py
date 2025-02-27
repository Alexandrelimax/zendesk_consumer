import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class GroupsClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/groups"
        self.max_threads = 5

    def fetch_page(self, params):
        response = self.request("GET", self.endpoint, params=params)
        groups = response.get("groups", [])
        meta = response.get("meta", {})

        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return groups, meta.get("after_cursor"), meta.get("has_more", False)

    def get_all_groups(self):
        all_groups = []
        pages_to_fetch = []
        params = {}

        groups, after_cursor, has_more = self.fetch_page(params)
        all_groups.extend(groups)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())
            _, after_cursor, has_more = self.fetch_page(params)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                groups, _, _ = future.result()
                all_groups.extend(groups)

        df = pd.DataFrame(all_groups)
        return df
