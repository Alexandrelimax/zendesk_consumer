from app.clients.endpoints.attachments_client import AttachmentsClient

class AttachmentsService:
    def __init__(self, client: AttachmentsClient):
        self.client = client

    def get_attachments(self):
        return self.client.get_attachments()

    def get_attachment_by_id(self, attachment_id: int):
        return self.client.get_attachment(attachment_id)

    def upload_attachment(self, file_data: dict):
        return self.client.upload_attachment(file_data)
