from app.clients.zendesk_client import ZendeskClient

class MessagesClient(ZendeskClient):
    def get_messages(self):
        return self.request("GET", "/api/v2/messages.json")

    def get_message(self, message_id: int):
        return self.request("GET", f"/api/v2/messages/{message_id}.json")

    def create_message(self, message_data: dict):
        return self.request("POST", "/api/v2/messages.json", data=message_data)
