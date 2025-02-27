from app.repositories.base_repository import BaseRepository
from google.cloud.bigquery import SchemaField

class MessagesRepository(BaseRepository):
    def __init__(self):
        schema = [
            SchemaField("id", "INTEGER"),
            SchemaField("conversation_id", "INTEGER"),
            SchemaField("sender_id", "INTEGER"),
            SchemaField("content", "STRING"),
            SchemaField("created_at", "TIMESTAMP"),
        ]
        super().__init__("messages", schema)

    def save_messages(self, df):
        """Salva mensagens no BigQuery."""
        self.save_dataframe(df)
