from app.clients.zendesk_client import ZendeskClient

class ConversationsClient(ZendeskClient):
    def get_conversations(self):
        return self.request("GET", "/api/v2/conversations.json")

    def get_conversation(self, conversation_id: int):
        return self.request("GET", f"/api/v2/conversations/{conversation_id}.json")

    def create_conversation(self, conversation_data: dict):
        return self.request("POST", "/api/v2/conversations.json", data=conversation_data)
