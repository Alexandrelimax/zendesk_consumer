from app.clients.endpoints.calls_client import CallsClient

class CallsService:
    def __init__(self, client: CallsClient):
        self.client = client

    def get_calls(self):
        return self.client.get_calls()

    def get_call_by_id(self, call_id: int):
        return self.client.get_call(call_id)

    def create_call(self, call_data: dict):
        return self.client.create_call(call_data)
