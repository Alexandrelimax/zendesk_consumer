from app.clients.zendesk_client import ZendeskClient

class TicketsClient(ZendeskClient):
    def get_tickets(self):
        return self.request("GET", "/api/v2/tickets.json")

    def get_ticket(self, ticket_id: int):
        return self.request("GET", f"/api/v2/tickets/{ticket_id}.json")

    def create_ticket(self, ticket_data: dict):
        return self.request("POST", "/api/v2/tickets.json", data=ticket_data)
