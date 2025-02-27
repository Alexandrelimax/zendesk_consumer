from app.clients.zendesk_client import ZendeskClient

class UsersClient(ZendeskClient):
    def get_users(self):
        return self.request("GET", "/api/v2/users.json")

    def get_user(self, user_id: int):
        return self.request("GET", f"/api/v2/users/{user_id}.json")

    def create_user(self, user_data: dict):
        return self.request("POST", "/api/v2/users.json", data=user_data)
