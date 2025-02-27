from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.conversations_service import ConversationsService
from app.models.conversations_model import Conversation
from typing import List

class ConversationsController(BaseController):
    def __init__(self, service: ConversationsService):
        self.service = service
        super().__init__(prefix="/conversations")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_conversations, methods=["GET"], response_model=List[Conversation])
        self.router.add_api_route("/{conversation_id}", self.get_conversation, methods=["GET"], response_model=Conversation)
        self.router.add_api_route("/", self.create_conversation, methods=["POST"], response_model=Conversation)

    def get_conversations(self) -> List[Conversation]:
        return self.service.get_conversations()

    def get_conversation(self, conversation_id: int) -> Conversation:
        conversation = self.service.get_conversation_by_id(conversation_id)
        if not conversation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Conversa não encontrada")
        return conversation

    def create_conversation(self, conversation: Conversation) -> Conversation:
        return self.service.create_conversation(conversation)
