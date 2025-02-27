from app.clients.endpoints.messages_client import MessagesClient

class MessagesService:
    def __init__(self, client: MessagesClient):
        self.client = client

    def get_messages(self):
        return self.client.get_messages()

    def get_message_by_id(self, message_id: int):
        return self.client.get_message(message_id)

    def create_message(self, message_data: dict):
        return self.client.create_message(message_data)
