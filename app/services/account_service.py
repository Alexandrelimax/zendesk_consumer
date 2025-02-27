from app.clients.endpoints.account_client import AccountClient

class AccountService:
    def __init__(self, client: AccountClient):
        self.client = client

    def get_account_info(self):
        return self.client.get_account_info()

    def update_account_info(self, account_data: dict):
        return self.client.update_account_info(account_data)
