from app.controllers.base_controller import BaseController
from fastapi import HTTPException, status
from app.services.attachments_service import AttachmentsService
from app.models.attachments_model import Attachment
from typing import List

class AttachmentsController(BaseController):
    def __init__(self, service: AttachmentsService):
        self.service = service
        super().__init__(prefix="/attachments")
        self.register_routes()

    def register_routes(self):
        self.router.add_api_route("/", self.get_attachments, methods=["GET"], response_model=List[Attachment])
        self.router.add_api_route("/{attachment_id}", self.get_attachment, methods=["GET"], response_model=Attachment)
        self.router.add_api_route("/", self.create_attachment, methods=["POST"], response_model=Attachment)

    def get_attachments(self) -> List[Attachment]:
        return self.service.get_attachments()

    def get_attachment(self, attachment_id: int) -> Attachment:
        attachment = self.service.get_attachment_by_id(attachment_id)
        if not attachment:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Anexo não encontrado")
        return attachment

    def create_attachment(self, attachment: Attachment) -> Attachment:
        return self.service.create_attachment(attachment)
