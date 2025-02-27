from app.clients.endpoints.tickets_client import TicketsClient
from app.repositories.tickets_repository import TicketsRepository

class TicketsService:
    def __init__(self, client: TicketsClient, repository: TicketsRepository):
        self.client = client
        self.repository = repository

    def get_and_store_tickets(self):
        """Busca tickets no Zendesk e salva no BigQuery"""
        tickets = self.client.get_tickets()["tickets"]
        self.repository.save_tickets(tickets)
        return {"message": "Tickets do Zendesk salvos no BigQuery!"}
