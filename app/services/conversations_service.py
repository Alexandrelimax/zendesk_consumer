from app.clients.endpoints.conversations_client import ConversationsClient

class ConversationsService:
    def __init__(self, client: ConversationsClient):
        self.client = client

    def get_conversations(self):
        return self.client.get_conversations()

    def get_conversation_by_id(self, conversation_id: int):
        return self.client.get_conversation(conversation_id)

    def create_conversation(self, conversation_data: dict):
        return self.client.create_conversation(conversation_data)
