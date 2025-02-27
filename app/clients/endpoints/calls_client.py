from app.clients.zendesk_client import ZendeskClient

class CallsClient(ZendeskClient):
    def get_calls(self):
        return self.request("GET", "/api/v2/calls.json")

    def get_call(self, call_id: int):
        return self.request("GET", f"/api/v2/calls/{call_id}.json")

    def create_call(self, call_data: dict):
        return self.request("POST", "/api/v2/calls.json", data=call_data)
