from app.clients.endpoints.users_client import UsersClient

class UsersService:
    def __init__(self, client: UsersClient):
        self.client = client

    def get_users(self):
        return self.client.get_users()

    def get_user_by_id(self, user_id: int):
        return self.client.get_user(user_id)

    def create_user(self, user_data: dict):
        return self.client.create_user(user_data)
