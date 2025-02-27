from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.users_service import UsersService
from app.models.users_model import User
from typing import List

class UsersController(BaseController):
    def __init__(self, service: UsersService):
        self.service = service
        super().__init__(prefix="/users")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_users, methods=["GET"], response_model=List[User])
        self.router.add_api_route("/{user_id}", self.get_user, methods=["GET"], response_model=User)
        self.router.add_api_route("/", self.create_user, methods=["POST"], response_model=User)

    def get_users(self) -> List[User]:
        return self.service.get_users()

    def get_user(self, user_id: int) -> User:
        user = self.service.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
        return user

    def create_user(self, user: User) -> User:
        return self.service.create_user(user)
