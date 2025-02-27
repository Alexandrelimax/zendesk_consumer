from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class AttachmentsRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("file_name", "STRING"),
            SchemaField("file_size", "INTEGER"),
            SchemaField("content_type", "STRING"),
            SchemaField("url", "STRING"),
            SchemaField("ticket_id", "INTEGER"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("attachments", schema)

    def save_attachments(self, df):
        """Salva anexos no BigQuery."""
        self.save_dataframe(df)
