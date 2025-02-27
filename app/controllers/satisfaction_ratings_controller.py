from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.satisfaction_ratings_service import SatisfactionRatingsService
from app.models.satisfaction_ratings_model import SatisfactionRating
from typing import List

class SatisfactionRatingsController(BaseController):
    def __init__(self, service: SatisfactionRatingsService):
        self.service = service
        super().__init__(prefix="/satisfaction_ratings")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_ratings, methods=["GET"], response_model=List[SatisfactionRating])
        self.router.add_api_route("/{rating_id}", self.get_rating, methods=["GET"], response_model=SatisfactionRating)
        self.router.add_api_route("/", self.create_rating, methods=["POST"], response_model=SatisfactionRating)

    def get_ratings(self) -> List[SatisfactionRating]:
        return self.service.get_ratings()

    def get_rating(self, rating_id: int) -> SatisfactionRating:
        rating = self.service.get_rating_by_id(rating_id)
        if not rating:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliação de satisfação não encontrada")
        return rating

    def create_rating(self, rating: SatisfactionRating) -> SatisfactionRating:
        return self.service.create_rating(rating)
