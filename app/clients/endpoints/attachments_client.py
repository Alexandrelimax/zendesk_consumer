from app.clients.zendesk_client import ZendeskClient

class AttachmentsClient(ZendeskClient):
    def get_attachments(self):
        return self.request("GET", "/api/v2/attachments.json")

    def get_attachment(self, attachment_id: int):
        return self.request("GET", f"/api/v2/attachments/{attachment_id}.json")

    def upload_attachment(self, file_data: dict):
        return self.request("POST", "/api/v2/uploads.json", data=file_data)
