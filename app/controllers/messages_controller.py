from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.messages_service import MessagesService
from app.models.messages_model import Message
from typing import List

class MessagesController(BaseController):
    def __init__(self, service: MessagesService):
        self.service = service
        super().__init__(prefix="/messages")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_messages, methods=["GET"], response_model=List[Message])
        self.router.add_api_route("/{message_id}", self.get_message, methods=["GET"], response_model=Message)
        self.router.add_api_route("/", self.create_message, methods=["POST"], response_model=Message)

    def get_messages(self) -> List[Message]:
        return self.service.get_messages()

    def get_message(self, message_id: int) -> Message:
        message = self.service.get_message_by_id(message_id)
        if not message:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Mensagem não encontrada")
        return message

    def create_message(self, message: Message) -> Message:
        return self.service.create_message(message)
