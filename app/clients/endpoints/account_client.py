from app.clients.zendesk_client import ZendeskClient

class AccountClient(ZendeskClient):
    def get_account_info(self):
        return self.request("GET", "/api/v2/account.json")

    def update_account_info(self, account_data: dict):
        return self.request("PUT", "/api/v2/account.json", data=account_data)
