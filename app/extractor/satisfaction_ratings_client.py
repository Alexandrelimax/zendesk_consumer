import pandas as pd
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from app.clients.zendesk_client import ZendeskClient

class SatisfactionRatingsClient(ZendeskClient):
    def __init__(self):
        super().__init__()
        self.endpoint = "/api/v2/satisfaction_ratings"
        self.max_threads = 5

    def fetch_page(self, params):
        response = self.request("GET", self.endpoint, params=params)
        ratings = response.get("satisfaction_ratings", [])
        meta = response.get("meta", {})

        if "Retry-After" in response.headers:
            wait_time = int(response.headers["Retry-After"])
            print(f"Rate limit atingido! Aguardando {wait_time} segundos...")
            time.sleep(wait_time)

        return ratings, meta.get("after_cursor"), meta.get("has_more", False)

    def get_all_ratings(self):
        all_ratings = []
        pages_to_fetch = []
        params = {}

        ratings, after_cursor, has_more = self.fetch_page(params)
        all_ratings.extend(ratings)

        while has_more:
            params["after_cursor"] = after_cursor
            pages_to_fetch.append(params.copy())
            _, after_cursor, has_more = self.fetch_page(params)

        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            future_to_params = {executor.submit(self.fetch_page, p): p for p in pages_to_fetch}
            for future in as_completed(future_to_params):
                ratings, _, _ = future.result()
                all_ratings.extend(ratings)

        df = pd.DataFrame(all_ratings)
        return df
