from app.clients.endpoints.satisfaction_ratings_client import SatisfactionRatingsClient

class SatisfactionRatingsService:
    def __init__(self, client: SatisfactionRatingsClient):
        self.client = client

    def get_ratings(self):
        return self.client.get_ratings()

    def get_rating_by_id(self, rating_id: int):
        return self.client.get_rating(rating_id)

    def create_rating(self, rating_data: dict):
        return self.client.create_rating(rating_data)
