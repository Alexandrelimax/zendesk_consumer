from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.tickets_service import TicketsService
from app.models.tickets_model import Ticket
from typing import List

class TicketsController(BaseController):
    def __init__(self, service: TicketsService):
        self.service = service
        super().__init__(prefix="/tickets")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_tickets, methods=["GET"], response_model=List[Ticket])
        self.router.add_api_route("/{ticket_id}", self.get_ticket, methods=["GET"], response_model=Ticket)
        self.router.add_api_route("/", self.create_ticket, methods=["POST"], response_model=Ticket)

    def get_tickets(self) -> List[Ticket]:
        return self.service.get_tickets()

    def get_ticket(self, ticket_id: int) -> Ticket:
        ticket = self.service.get_ticket_by_id(ticket_id)
        if not ticket:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket não encontrado")
        return ticket

    def create_ticket(self, ticket: Ticket) -> Ticket:
        return self.service.create_ticket(ticket)
