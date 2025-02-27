from app.clients.zendesk_client import ZendeskClient

class SatisfactionRatingsClient(ZendeskClient):
    def get_ratings(self):
        return self.request("GET", "/api/v2/satisfaction_ratings.json")

    def get_rating(self, rating_id: int):
        return self.request("GET", f"/api/v2/satisfaction_ratings/{rating_id}.json")

    def create_rating(self, rating_data: dict):
        return self.request("POST", "/api/v2/satisfaction_ratings.json", data=rating_data)
